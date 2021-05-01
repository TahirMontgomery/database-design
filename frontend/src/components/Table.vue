<template>
  <div>
    <mdb-tbl bordered>
      <mdb-tbl-head>
        <tr>
          <th v-for="col in data.cols" :key="col.name">
            {{ col.name }}
          </th>
          <th>{{ "" }}</th>
        </tr>
      </mdb-tbl-head>
      <mdb-tbl-body>
        <tr v-for="row in paginateData()" :key="row.id">
          <td v-for="key in sortKeys(row)" :key="key">
            {{ row[key] }}
          </td>
          <td class="text-center">
            <mdb-tooltip
              v-if="!admin && !disabled"
              trigger="hover"
              :options="{ placement: 'top' }"
            >
              <span slot="tip"> Dispute Transaction </span>
              <span slot="reference" class="dispute" @click="dispute(row.id)"
                ><mdb-icon color="danger" icon="ban"
              /></span>
            </mdb-tooltip>
            <mdb-tooltip
              v-else-if="admin"
              trigger="hover"
              :options="{ placement: 'top' }"
            >
              <span slot="tip"> Review Dispute </span>
              <span
                slot="reference"
                class="dispute"
                @click="reviewDispute(row.id)"
                ><mdb-icon size="lg" color="danger" icon="edit"
              /></span>
            </mdb-tooltip>
          </td>
        </tr>
      </mdb-tbl-body>
    </mdb-tbl>
    <mdb-pagination>
      <span @click="paginatePrev()">
        <mdb-page-nav prev></mdb-page-nav>
      </span>
      <span v-for="x in paginateMax" @click="index = x" :key="x">
        <mdb-page-item :active="x == index">
          {{ x }}
        </mdb-page-item>
      </span>
      <span @click="paginateNext()">
        <mdb-page-nav next></mdb-page-nav>
      </span>
    </mdb-pagination>
    <mdb-modal :show="show" @close="show = false">
      <mdb-modal-header>
        <mdb-modal-title>{{ modalTitle }}</mdb-modal-title>
      </mdb-modal-header>
      <mdb-modal-body>
        <h5>Merchant: {{ store }}</h5>
        <h5>Price: ${{ Number(amount).toFixed(2) }}</h5>
        <h5 v-if="admin">Reason: {{ reason }}</h5>
        <hr />
        <mdb-input
          placeholder="Please enter any comments."
          type="textarea"
          rows="5"
          outline
          v-model="disputeReason"
        ></mdb-input>
      </mdb-modal-body>
      <mdb-modal-footer>
        <mdb-btn color="success" @click="handleDispute('Approved')">{{
          admin ? "Approve" : "Submit"
        }}</mdb-btn>
        <mdb-btn
          color="danger"
          @click="admin ? handleDispute('Rejected') : (show = false)"
          >{{ admin ? "Reject" : "Cancel" }}</mdb-btn
        >
      </mdb-modal-footer>
    </mdb-modal>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Table",
  props: ["data", "admin", "disabled"],
  data() {
    return {
      rowAmount: 10,
      index: 1,
      paginateMax: 1,
      show: false,
      store: "",
      amount: 0,
      reason: "",
      disputeReason: "",
      modalTitle: "",
      activeTransactionId: null,
    };
  },
  created() {
    this.getPaginate();
  },
  methods: {
    getPaginate() {
      if (this.data.rows.length > this.rowAmount) {
        this.paginateMax = Math.floor(this.data.rows.length / 10) + 1;
      }
    },
    sortKeys() {
      let keys = [];
      this.data.cols.forEach((col) => {
        keys.push(col.name.toLowerCase());
      });
      return keys;
    },
    async handleDispute(status) {
      if (this.admin) {
        try {
          console.log(this.activeTransactionId);
          await axios.post(
            "https://bank-usf.herokuapp.com/disputes/reviewdisputes/",
            {
              tid: Number(this.activeTransactionId),
              status: status,
              admin_comments: this.disputeReason,
            }
          );
          this.$emit("refresh");
          this.show = false;
          alert("Dispute review was successful");
          return;
        } catch (err) {
          console.log(err);
        }
      } else {
        try {
          console.log(this.disputeReason, this.activeTransactionId);
          const response = await axios.post(
            "https://bank-usf.herokuapp.com/disputes/makedispute/",
            {
              tid: Number(this.activeTransactionId),
              status: "Pending",
              user_reason: this.disputeReason,
            }
          );
          console.log(response);
          this.$emit("refresh");
          this.show = false;
          alert("Dispute request was successful");
        } catch (err) {
          console.log(err);
        }
      }
    },
    dispute(id) {
      const transaction = this.data.rows.filter((row) => row.id == id)[0];
      this.activeTransactionId = transaction.id;
      this.store = transaction.store;
      this.amount = transaction.amount;
      this.modalTitle = "Dispute";
      this.show = true;
    },
    change(x) {
      console.log(x);
    },
    paginateData() {
      this.getPaginate();
      if (this.data.rows.length <= this.rowAmount) {
        return this.data.rows;
      }

      let startIndex = (this.index - 1) * this.rowAmount;
      let endIndex = startIndex + this.rowAmount;
      return this.data.rows.slice(startIndex, endIndex);
    },
    paginateNext() {
      if (this.index == this.paginateMax) {
        this.index = 1;
      } else {
        this.index++;
      }
    },
    paginatePrev() {
      if (this.index == 1) {
        return;
      } else {
        this.index--;
      }
    },
    reviewDispute(tid) {
      const transaction = this.data.rows.filter((row) => row.id == tid)[0];
      this.activeTransactionId = transaction.id;
      this.store = transaction.store;
      this.amount = transaction.amount;
      this.reason = transaction.user_reason;
      this.modalTitle = "Review Dispute";
      this.show = true;
    },
  },
};
</script>

<style>
.dispute:hover {
  cursor: pointer;
}
</style>

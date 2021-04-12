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
              v-if="!admin"
              trigger="hover"
              :options="{ placement: 'top' }"
            >
              <span slot="tip"> Dispute Transaction </span>
              <span
                slot="reference"
                class="dispute"
                @click="reviewDispute(row.id)"
                ><mdb-icon color="danger" icon="ban"
              /></span>
            </mdb-tooltip>
            <mdb-tooltip v-else trigger="hover" :options="{ placement: 'top' }">
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
        <mdb-modal-title>Review Dispute</mdb-modal-title>
      </mdb-modal-header>
      <mdb-modal-body>
        <h5>Merchant: Apple Store</h5>
        <h5>Price: $25.00</h5>
        <h5>Date: April 5, 2021</h5>
        <h5>Reason: I did not authorize this transaction</h5>
        <hr />
        <mdb-input
          placeholder="Please enter any comments. This is not required"
          type="textarea"
          rows="5"
          outline
        ></mdb-input>
      </mdb-modal-body>
      <mdb-modal-footer>
        <mdb-btn color="success">Approve</mdb-btn>
        <mdb-btn color="danger">Reject</mdb-btn>
      </mdb-modal-footer>
    </mdb-modal>
  </div>
</template>

<script>
export default {
  name: "Table",
  props: ["data", "admin"],
  data() {
    return {
      rowAmount: 10,
      index: 1,
      paginateMax: 1,
      show: false,
    };
  },
  created() {
    if (this.data.rows.length > this.rowAmount) {
      this.paginateMax = Math.floor(this.data.rows.length / 10) + 1;
    }
  },
  methods: {
    sortKeys() {
      let keys = [];
      this.data.cols.forEach((col) => {
        keys.push(col.name.toLowerCase());
      });
      return keys;
    },
    dispute(id) {
      console.log(id);
    },
    change(x) {
      console.log(x);
    },
    paginateData() {
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
      console.log(tid);
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

<template>
  <div>
    <mdb-container class="mt-4" fluid>
      <h1>Resolve Disputes</h1>
      <mdb-row class="mt-5">
        <mdb-col>
          <h2>Pending Disputes</h2>
          <Table
            @refresh="getDisputes"
            :admin="true"
            :data="pendingDisputeData"
          />
        </mdb-col>
        <mdb-col>
          <h2>Dispute History</h2>
          <Table :disabled="true" :data="disputeData" />
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
import Table from "@/components/Table.vue";
import axios from "axios";
export default {
  name: "Admin",
  components: {
    Table,
  },
  data() {
    return {
      disputeData: {
        cols: [
          {
            name: "ID",
          },
          {
            name: "Status",
          },
          {
            name: "Store",
          },
          {
            name: "User_reason",
          },
          {
            name: "Admin_comments",
          },
          {
            name: "Amount",
          },
        ],
        rows: [],
      },
      pendingDisputeData: {
        cols: [
          {
            name: "ID",
          },
          {
            name: "Status",
          },
          {
            name: "Store",
          },
          {
            name: "User_reason",
          },
          {
            name: "Admin_comments",
          },
          {
            name: "Amount",
          },
        ],
        rows: [],
      },
    };
  },
  created() {
    this.getDisputes();
  },
  methods: {
    async getDisputes() {
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_URL}/disputes/getalldisputes/`
        );
        const trans = await axios.post(
          `${process.env.VUE_APP_URL}/transactions/getalltransactions/`
        );
        this.disputeData.rows = response.data.map((row) => ({
          id: row.tid,
          status: row.status,
          user_reason: row.user_reason,
          admin_comments: row.admin_comments,
          store: this.getTransactionById(trans.data, row.tid)?.store_name,
          amount: this.getTransactionById(trans.data, row.tid)?.amount,
        }));

        this.pendingDisputeData.rows = [];
        response.data.forEach((row) => {
          if (row.status == "Pending") {
            this.pendingDisputeData.rows.push({
              id: row.tid,
              status: row.status,
              user_reason: row.user_reason,
              admin_comments: row.admin_comments,
              store: this.getTransactionById(trans.data, row.tid)?.store_name,
              amount: this.getTransactionById(trans.data, row.tid)?.amount,
            });
          }
          return;
        });
      } catch (error) {
        console.log(error);
      }
    },
    getTransactionById(data, id) {
      const transIndex = data.findIndex((row) => row.tid == id);
      if (transIndex >= 0) {
        return data[transIndex];
      }
      return null;
    },
  },
};
</script>

<style></style>

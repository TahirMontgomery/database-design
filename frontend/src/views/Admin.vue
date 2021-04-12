<template>
  <div>
    <mdb-container class="mt-4" fluid>
      <h1>Resolve Disputes</h1>
      <mdb-row class="mt-5">
        <mdb-col>
          <h2>Pending Disputes</h2>
          <Table :admin="true" :data="disputeData" />
        </mdb-col>
        <mdb-col>
          <h2>Dispute History</h2>
          <Table :admin="true" :data="disputeData" />
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
import Table from "@/components/Table.vue";

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
            name: "Store",
          },
          {
            name: "Amount",
          },
          {
            name: "Status",
          },
        ],
        rows: [
          {
            id: 1,
            store: "Apple",
            amount: 20,
            status: "PENDING",
          },
        ],
      },
    };
  },
};
</script>

<style></style>

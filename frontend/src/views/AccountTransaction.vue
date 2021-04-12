<template>
  <div>
    <mdb-container class="mt-5" fluid>
      <h1>{{ accountName }}</h1>

      <mdb-row class="mt-5">
        <mdb-col cols="6">
          <h3 class="text-left">All Transactions</h3>
          <Table :data="transactionData" />
        </mdb-col>
        <mdb-col cols="6">
          <h3 class="text-left">All Disputes</h3>
          <Table :data="disputeData" />
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
import moment from "moment";
import Table from "@/components/Table.vue";
export default {
  name: "AccountTransaction",
  components: {
    Table,
  },
  methods: {
    getFakeData(num) {
      return new Array(num).fill(null).map(() => ({
        id: this.faker.datatype.uuid(),
        account: this.faker.finance.accountName(),
        amount: this.faker.finance.amount(),
        store: this.faker.company.companyName(),
        date: moment(this.faker.date.past()).format("MMMM Do YYYY, h:mm:ss a"),
      }));
    },
  },
  data() {
    return {
      accountName: "Retirement Savings Account",
      transactionData: {
        cols: [
          {
            name: "Account",
          },
          {
            name: "Amount",
          },
          {
            name: "Store",
          },
          {
            name: "Date",
          },
        ],
        rows: this.getFakeData(3),
      },
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

<template>
  <div class="home">
    <mdb-container fluid>
      <mdb-row class="mt-4">
        <mdb-col>
          <BalanceCard
            :cardTitle="'Total Balance'"
            :cardSubtitle="`$${totalBalance}`"
            color="lightRed"
            cardIcon="dollar-sign"
          />
        </mdb-col>
        <mdb-col>
          <BalanceCard
            color="blue"
            :cardTitle="'# of Transactions'"
            :cardSubtitle="totalTransactions"
            cardIcon="exchange-alt"
          />
        </mdb-col>
        <mdb-col>
          <BalanceCard
            color="maroon"
            :cardTitle="'Total Disputes'"
            :cardSubtitle="totalDisputes"
            cardIcon="ban"
          />
        </mdb-col>
      </mdb-row>
      <mdb-row class="mt-5">
        <mdb-col cols="6">
          <h3 class="text-left">Recent Transactions</h3>
          <Table @refresh="getDisputes" :data="transactionData" />
        </mdb-col>
        <mdb-col cols="6">
          <h3 class="text-left">Recent Disputes</h3>
          <Table :disabled="true" :data="disputeData" />
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
// @ is an alias to /src
import moment from "moment";
import BalanceCard from "@/components/BalanceCard.vue";
import Table from "@/components/Table.vue";
import axios from "axios";
export default {
  name: "Home",
  components: {
    BalanceCard,
    Table,
  },
  methods: {
    randomName() {
      return this.faker.finance.accountName();
    },
    getFakeData(num) {
      return new Array(num).fill(null).map(() => ({
        id: this.faker.datatype.uuid(),
        account: this.faker.finance.accountName(),
        amount: this.faker.finance.amount(),
        store: this.faker.company.companyName(),
        date: moment(this.faker.date.past()).format("MMMM Do YYYY, h:mm:ss a"),
      }));
    },

    async getTransactions() {
      const response = await axios.post(
        `${process.env.VUE_APP_URL}/transactions/getusertransactions/`,
        { uid: this.$store.state.user.uid }
      );
      this.transactionData.rows = response.data.map((row) => ({
        id: row.tid,
        store: row.store_name,
        amount: row.amount,
        status: row.status,
      }));

      this.totalTransactions = this.transactionData.rows.length;
    },
    async getAccounts() {
      const response = await axios.post(
        `${process.env.VUE_APP_URL}/accounts/getallaccounts/`
      );
      let balance = 0;
      response.data.forEach((acc) => {
        if (acc.uid == this.$store.state.user.uid) {
          balance += acc.balance;
        }
      });
      this.totalBalance = balance;
    },
    async getDisputes() {
      const response = await axios.post(
        `${process.env.VUE_APP_URL}/disputes/getuserdisputes/`,
        {
          uid: this.$store.state.user.uid,
        }
      );
      this.disputeData.rows = response.data.map((row) => ({
        id: row.tid,
        status: row.status,
        store: this.getTransactionById(row.tid)?.store,
        amount: this.getTransactionById(row.tid)?.amount,
        user_reason: row.user_reason,
        admin_comments: row.admin_comments,
      }));

      this.totalDisputes = this.disputeData.rows.length;
    },
    getTransactionById(id) {
      const trans = this.transactionData.rows.findIndex((row) => row.id == id);
      if (trans >= 0) {
        return this.transactionData.rows[trans];
      }
      return null;
    },
  },
  async created() {
    await this.getTransactions();
    await this.getAccounts();
    await this.getDisputes();
  },
  data() {
    return {
      totalBalance: 0,
      totalTransactions: 0,
      totalDisputes: 0,

      transactionData: {
        cols: [
          {
            name: "ID",
          },
          {
            name: "Amount",
          },
          {
            name: "Store",
          },
          {
            name: "Status",
          },
        ],
        rows: [],
      },
      disputeData: {
        cols: [
          {
            name: "ID",
          },
          {
            name: "Store",
          },
          {
            name: "Amount",
          },
          {
            name: "Status",
          },
          {
            name: "User_Reason",
          },
          {
            name: "Admin_Comments",
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

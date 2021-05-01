<template>
  <div>
    <mdb-container class="mt-5" fluid>
      <h1>{{ accountName }}</h1>
      <h1>Account Balance: ${{ accountBalance }}</h1>
      <h1>Account Type: {{ accountType }}</h1>
      <mdb-btn color="mdb-color darken-1" @click="open1 = true"
        >Add transaction</mdb-btn
      >
      <mdb-btn color="green darken-1" @click="open2 = true">Withdraw</mdb-btn>
      <mdb-btn color="red darken-1" @click="open3 = true">Deposit</mdb-btn>

      <mdb-modal :show="open1" @close="open1 = false">
        <mdb-modal-header>
          <mdb-modal-title>Add Transaction</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body>
          <mdb-input
            label="Store Name"
            v-model="transaction.store_name"
            placeholder="Please enter store name"
            type="text"
            outline
          ></mdb-input>
          <mdb-input
            label="Enter Transaction amount"
            outline
            type="number"
            v-model="transaction.amount"
          />
        </mdb-modal-body>
        <mdb-modal-footer>
          <mdb-btn color="success" @click="addTransaction">Add</mdb-btn>
          <mdb-btn color="danger" @click="open1 = false">Cancel</mdb-btn>
        </mdb-modal-footer>
      </mdb-modal>
      <mdb-modal :show="open2" @close="open2 = false">
        <mdb-modal-header>
          <mdb-modal-title>Withdraw</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body>
          <mdb-input
            label="Enter amount to withdraw"
            outline
            type="number"
            v-model="withdrawalAmount"
          />
        </mdb-modal-body>
        <mdb-modal-footer>
          <mdb-btn color="success" @click="withdraw">Withdraw</mdb-btn>
          <mdb-btn color="danger" @click="open2 = false">Cancel</mdb-btn>
        </mdb-modal-footer>
      </mdb-modal>
      <mdb-modal :show="open3" @close="open3 = false">
        <mdb-modal-header>
          <mdb-modal-title>Deposit</mdb-modal-title>
        </mdb-modal-header>
        <mdb-modal-body>
          <mdb-input
            label="Enter amount to deposit"
            outline
            type="number"
            v-model="depositAmount"
          />
        </mdb-modal-body>
        <mdb-modal-footer>
          <mdb-btn color="success" @click="deposit">Deposit</mdb-btn>
          <mdb-btn color="danger" @click="open3 = false">Cancel</mdb-btn>
        </mdb-modal-footer>
      </mdb-modal>
      <mdb-row class="mt-5">
        <mdb-col cols="6">
          <h3 class="text-left">All Transactions</h3>
          <Table
            @refresh="
              () => {
                this.getDisputes();
                this.getTransactions();
              }
            "
            :admin="false"
            :data="transactionData"
          />
        </mdb-col>
        <mdb-col cols="6">
          <h3 class="text-left">All Disputes</h3>
          <Table :admin="false" disabled="true" :data="disputeData" />
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";
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
    async getDisputes() {
      const response = await axios.post(
        `${process.env.VUE_APP_URL}/disputes/getaccountdisputes/`,
        {
          uid: this.$store.state.user.uid,
          account_id: this.$route.query.accountId,
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
    },
    getTransactionById(id) {
      const trans = this.transactionData.rows.findIndex((row) => row.id == id);
      if (trans >= 0) {
        console.log("hey", this.transactionData.rows[trans]);
        return this.transactionData.rows[trans];
      }
      return null;
    },
    async getTransactions() {
      const response = await axios.post(
        `${process.env.VUE_APP_URL}/transactions/getaccounttransactions/`,
        {
          uid: this.$store.state.user.uid,
          account_id: this.$route.query.accountId,
        }
      );
      this.transactionData.rows = response.data.map((row) => ({
        id: row.tid,
        store: row.store_name,
        amount: row.amount,
        status: row.status,
      }));
    },
    async addTransaction() {
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_URL}/transactions/createtransaction/`,
          {
            uid: this.$store.state.user.uid,
            account_id: this.$route.query.accountId,
            status: "Complete",
            ...this.transaction,
          }
        );
        console.log(response);
        this.accountBalance -= Number(this.transaction.amount);
        this.getTransactions();
        this.open1 = false;
      } catch (err) {
        console.log(err);
        alert("Error trying to add transaction");
      }
    },
    async withdraw() {
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_URL}/transactions/makewithdrawal/`,
          {
            uid: this.$store.state.user.uid,
            account_id: this.$route.query.accountId,
            status: "Complete",
            amount: this.withdrawalAmount,
          }
        );
        console.log(response);
        this.accountBalance -= Number(this.withdrawalAmount);
        this.getTransactions();
        this.open2 = false;
      } catch (err) {
        console.log(err);
        alert("An error occurred. Could not complete request");
      }
    },
    async deposit() {
      try {
        await axios.post(
          `${process.env.VUE_APP_URL}/transactions/makedeposit/`,
          {
            uid: this.$store.state.user.uid,
            account_id: this.$route.query.accountId,
            status: "Complete",
            amount: this.depositAmount,
          }
        );
        this.accountBalance += Number(this.depositAmount);
        this.getTransactions();
        this.open3 = false;
      } catch (err) {
        console.log(err);
        alert("An error occurred. Could not complete request");
      }
    },
  },
  async created() {
    this.accountName = this.$route.query.accountName;
    this.accountBalance = this.$route.query.accountBalance;
    this.accountType = this.$route.query.accountType;
    await this.getTransactions();
    await this.getDisputes();
  },
  data() {
    return {
      accountName: "Retirement Savings Account",
      open1: false,
      open2: false,
      open3: false,
      withdrawalAmount: 0,
      depositAmount: 0,
      accountBalance: 0,
      transaction: {
        store_name: "",
        amount: 0,
      },
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

<style></style>

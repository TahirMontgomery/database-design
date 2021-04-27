<template>
  <div class="home">
    <mdb-container fluid>
      <mdb-btn color="mdb-color darken-3" @click="open = true"
        >Add account</mdb-btn
      >
      <mdb-row class="mt-4">
        <mdb-col>
          <BalanceCard
            :cardTitle="'Total Balance'"
            :cardSubtitle="'$100,000'"
            color="lightRed"
            cardIcon="dollar-sign"
          />
        </mdb-col>
        <mdb-col>
          <BalanceCard
            color="blue"
            :cardTitle="'# of Transactions'"
            :cardSubtitle="'88'"
            cardIcon="exchange-alt"
          />
        </mdb-col>
        <mdb-col>
          <BalanceCard
            color="maroon"
            :cardTitle="'Pending Disputes'"
            :cardSubtitle="'0'"
            cardIcon="ban"
          />
        </mdb-col>
      </mdb-row>
      <mdb-row class="mt-5">
        <mdb-col cols="6">
          <h3 class="text-left">Recent Transactions</h3>
          <Table :data="transactionData" />
        </mdb-col>
        <mdb-col cols="6">
          <h3 class="text-left">Recent Disputes</h3>
          <Table :data="disputeData" />
        </mdb-col>
      </mdb-row>
    </mdb-container>
    <mdb-modal :show="open" @close="open = false">
      <mdb-modal-header>
        <mdb-modal-title>Add Account</mdb-modal-title>
      </mdb-modal-header>
      <mdb-modal-body>
        <mdb-input
          label="Account Name"
          v-model="account.account_name"
          placeholder="Please enter account name"
          type="text"
          outline
        ></mdb-input>
        <select
          class="browser-default custom-select"
          v-model="account.account_type"
        >
          <option value="null">Select Account Type</option>
          <option value="Checking">Checking</option>
          <option value="Savings">Saving</option>
        </select>
        <mdb-input
          label="Enter Balance on this account"
          outline
          type="number"
          v-model="account.balance"
        />
      </mdb-modal-body>
      <mdb-modal-footer>
        <mdb-btn color="success" @click="addAccount">Add</mdb-btn>
        <mdb-btn color="danger">Cancel</mdb-btn>
      </mdb-modal-footer>
    </mdb-modal>
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
    async addAccount() {
      console.log(this.$store);
      try {
        const response = await axios.post(
          "https://bank-usf.herokuapp.com/accounts/createaccount/",
          {
            ...this.account,
            uid: this.$store.state.user.uid,
          }
        );
        console.log(response);
        this.alert("Account created successfully");
        this.open = false;
      } catch (err) {
        console.log(err);
        alert("Error occurred. Could not add account");
      }
    },
    async getTransactions() {
      const response = await axios.get(
        "https://bank-usf.herokuapp.com/transactions/getusertransactions/",
        {
          body: {
            uid: this.$store.state.user.uid,
          },
        }
      );
      console.log(response);
    },
  },
  async created() {
    this.getTransactions();
  },
  data() {
    return {
      open: false,
      account: {
        account_type: "null",
        account_name: "",
        balance: 0,
      },
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
        rows: [],
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

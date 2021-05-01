<template>
  <div class="">
    <mdb-container fluid>
      <mdb-btn color="mdb-color darken-3" @click="open = true"
        >Add account</mdb-btn
      >
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
            :cardTitle="'# of Accounts'"
            :cardSubtitle="`${totalAccounts}`"
            cardIcon="exchange-alt"
          />
        </mdb-col>
      </mdb-row>
      <h3 class="mt-5">Accounts</h3>

      <mdb-row>
        <mdb-col v-for="account in accounts" :key="account.id" col="4">
          <mdb-card class="text-left text-black">
            <mdb-card-body>
              <p>{{ account.account_name }}</p>
              <h2>Balance: ${{ account.balance }}</h2>
              <mdb-btn
                color="mdb-color darken-3"
                @click="
                  getTransactions(
                    account.account_id,
                    account.account_name,
                    account.balance,
                    account.account_type
                  )
                "
                >View Account</mdb-btn
              >
            </mdb-card-body>
          </mdb-card>
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </div>
</template>

<script>
import BalanceCard from "@/components/BalanceCard.vue";
import axios from "axios";
export default {
  name: "Accounts",
  components: {
    BalanceCard,
  },
  methods: {
    randomColor() {
      var randomColor = Math.floor(Math.random() * 16777215).toString(16);
      return `#${randomColor}`;
    },
    getTransactions(accountId, accountName, accountBalance, accountType) {
      console.log(accountType);
      this.$router.push({
        name: "AccountTransaction",
        query: { accountId, accountName, accountBalance, accountType },
      });
    },
    async addAccount() {
      console.log(this.$store);
      try {
        await axios.post(`${process.env.VUE_APP_URL}/accounts/createaccount/`, {
          ...this.account,
          uid: this.$store.state.user.uid,
        });
        alert("Account created successfully");
        this.getAccounts();
        this.open = false;
      } catch (err) {
        console.log(err);
        alert("Error occurred. Could not add account");
      }
    },
    async getAccounts() {
      const response = await axios.post(
        `${process.env.VUE_APP_URL}/accounts/getallaccounts/`
      );
      this.accounts = response.data.filter(
        (acc) => acc.uid == this.$store.state.user.uid
      );
      let balance = 0;
      response.data.forEach((acc) => {
        if (acc.uid == this.$store.state.user.uid) {
          balance += acc.balance;
        }
      });
      this.totalBalance = balance;
      this.totalAccounts = this.accounts.length;
    },
  },
  created() {
    this.getAccounts();
  },
  data() {
    return {
      open: false,
      totalBalance: 0,
      totalAccounts: 0,
      account: {
        account_type: "null",
        account_name: "",
        balance: 0,
      },
      accounts: [],
    };
  },
};
</script>

<style></style>

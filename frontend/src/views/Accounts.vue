<template>
  <div class="">
    <mdb-container fluid>
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
            :cardTitle="'# of Accounts'"
            :cardSubtitle="'3'"
            cardIcon="exchange-alt"
          />
        </mdb-col>
      </mdb-row>
      <h3 class="mt-5">Accounts</h3>

      <mdb-row>
        <mdb-col cols="4">
          <mdb-card class="text-left text-black">
            <mdb-card-body>
              <p>Retirement Savings Account</p>
              <h2>Balance: $100</h2>
              <mdb-btn color="mdb-color darken-3" @click="getTransactions(1)"
                >View Account</mdb-btn
              >
            </mdb-card-body>
          </mdb-card>
        </mdb-col>
        <mdb-col cols="4">
          <mdb-card class="text-left text-black">
            <mdb-card-body>
              <p>Retirement Savings Account</p>
              <h2>Balance: $100</h2>
              <mdb-btn color="mdb-color darken-3" @click="getTransactions(1)"
                >View Account</mdb-btn
              >
            </mdb-card-body>
          </mdb-card>
        </mdb-col>
        <mdb-col cols="4">
          <mdb-card class="text-left text-black">
            <mdb-card-body>
              <p>Retirement Savings Account</p>
              <h2>Balance: $100</h2>
              <mdb-btn color="mdb-color darken-3" @click="getTransactions(1)"
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
    getTransactions(accountId) {
      console.log(accountId);
      this.$router.push({ name: "AccountTransaction", query: { accountId } });
    },
  },
};
</script>

<style></style>

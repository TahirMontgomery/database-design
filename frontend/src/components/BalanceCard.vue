<template>
  <div :style="cardStyle" :class="cardClass">
    <div class="card__left">
      <h3 class="card__title">{{ cardTitle }}</h3>
      <h1 class="card__subtitle">{{ cardSubtitle }}</h1>
    </div>
    <div class="card__right">
      <mdb-icon class="text-white" size="3x" :icon="cardIcon" />
    </div>
  </div>
</template>

<script>
export default {
  name: "BalanceCard",
  props: [
    "cardTitle",
    "cardSubtitle",
    "cardPercent",
    "cardIcon",
    "size",
    "color",
  ],
  computed: {
    cardClass() {
      return {
        balance__card: true,
      };
    },
    cardStyle() {
      var styles = {
        lightRed: "linear-gradient(93.69deg, #FF6B6B 2.58%, #F06E6E 100%)",
        blue: "#33658a",
        maroon: "#8E4162",
      };
      return {
        background: styles[this.color] || "black",
      };
    },
  },
  methods: {},
};
</script>

<style>
.balance__card {
  border-radius: 20px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 120px;
  padding: 0 30px;
}

.card__title {
  font-size: 16px;
  font-weight: lighter;
  color: white;
  text-align: left;
}

.card__subtitle {
  font-size: 40px;
  font-weight: bold;
  color: white;
  letter-spacing: 1px;
  text-align: left;
}

.card__right span {
  font-size: 18px;
  color: white;
  font-weight: 400;
}
</style>

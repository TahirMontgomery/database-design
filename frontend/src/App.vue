<template>
  <div id="app">
    <sidebar-menu
      v-if="checkRoute"
      @toggle-collapse="onToggleCollapse"
      width="200px"
      :menu="menu"
    >
      <div slot="footer" class="text-center mb-3">
        <mdb-btn
          @click="$store.commit('logout')"
          color="danger"
          v-if="!collapsed"
          >Logout</mdb-btn
        >
      </div></sidebar-menu
    >
    <router-view :style="main" />
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  data() {
    return {
      collapsed: false,
    };
  },
  computed: {
    menu() {
      return [
        {
          header: true,
          title: "Database Design",
          hiddenOnCollapse: true,
        },
        {
          href: "/",
          title: "Home",
          icon: "fa fa-home",
          hidden: this.$store.state.user.role != "User",
        },
        {
          href: "/accounts",
          title: "Accounts",
          icon: "fa fa-user",
          hidden: this.$store.state.user.role != "User",
        },
        {
          href: "/admin",
          title: "Admin",
          icon: "fa fa-user",
          hidden: this.$store.state.user.role != "Admin",
        },
      ];
    },
    main() {
      return {
        marginLeft:
          this.collapsed && this.checkRoute
            ? "50px"
            : !this.checkRoute
            ? "0px"
            : !this.collapsed && this.checkRoute
            ? "200px"
            : "0",
        transition: "all .2s ease-in",
      };
    },
    checkRoute() {
      if (this.$route.path == "/login" || this.$route.path == "/register") {
        return false;
      }
      return true;
    },
  },
  created() {
    if (!this.$store.state.user.isLoggedIn) {
      this.$router.push("/login");
    }
  },
  methods: {
    onToggleCollapse(collapsed) {
      this.collapsed = collapsed;
    },
  },
  watch: {
    "$store.state.user.isLoggedIn": function () {
      console.log("Hey");
      if (this.$store.state.user.isLoggedIn) {
        if (this.$store.state.user.role == "Admin") {
          this.$router.push("/admin");
        } else {
          this.$router.push("/");
        }
      } else {
        this.$router.push("/login");
      }
    },
  },
};
</script>
<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap");

/* .v-sidebar-menu {
  background-color: lightgray !important;
} */

.v-sidebar-menu .vsm--icon {
  background: $primary-color !important;
}

.v-sidebar-menu .vsm--link.vsm--link_active {
  -webkit-box-shadow: 3px 0px 0px 0px $primary-color inset !important;
  box-shadow: 3px 0px 0px 0px $primary-color inset !important;
}
</style>

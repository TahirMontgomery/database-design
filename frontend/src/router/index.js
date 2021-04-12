import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import Login from "../views/Login.vue";
import Accounts from "../views/Accounts.vue";
import AccountTransaction from "../views/AccountTransaction.vue";
import Admin from "../views/Admin.vue";
import store from "../store";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/accounts",
    name: "Accounts",
    component: Accounts,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/accounts/transaction",
    name: "AccountTransaction",
    component: AccountTransaction,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  var requiresAuth = to.meta.requiresAuth;
  if ((requiresAuth && store.state.user.isLoggedIn) || !requiresAuth) {
    next();
  } else {
    next("/login");
  }
});

export default router;

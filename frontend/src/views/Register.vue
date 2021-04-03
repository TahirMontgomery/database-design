<template>
  <mdb-container fluid>
    <mdb-row class="full-height">
      <mdb-col class="left">
        <div class="register">
          <h2 class="font-weight-bold">Register</h2>
          <p class="lead">Please register your account</p>
          <div class="form">
            <!-- Email Input -->

            <mdb-input
              required
              id="first"
              type="text"
              label="Enter your first name"
              outline
              v-model="user.firstName"
            />
            <mdb-input
              required
              id="last"
              type="text"
              label="Enter your last name"
              outline
              v-model="user.lastName"
            />
            <mdb-input
              required
              id="email"
              type="email"
              label="Enter email"
              outline
              v-model="user.email"
            />

            <!-- Password Input -->
            <mdb-input
              id="password"
              type="password"
              label="Enter password"
              required
              outline
              v-model="user.password"
            />

            <mdb-input
              id="confirm"
              type="password"
              label="Confirm password"
              required
              outline
              v-model="user.confirm"
            />

            <!-- Submit Button -->
            <!-- Forgot Password -->
            <div class="forgot_and_register">
              <mdb-btn @click="register" id="login_btn" class="login_btn mr-3"
                >REGISTER</mdb-btn
              >
              <router-link class="link" to="/login"
                >Already have an account? Login here.</router-link
              >
            </div>

            <!-- Third Party Sign in -->
            <!-- <div class="third_party">
              <p>or</p>
              <div class="third_party_icons">
                <mdb-icon
                  class="mr-5 fb-logo"
                  size="3x"
                  fab
                  icon="facebook-square"
                />
                <mdb-icon
                  size="3x"
                  fab
                  icon="google-plus-square"
                  class="google-logo"
                />
              </div>
            </div> -->
          </div>
        </div>
      </mdb-col>
      <mdb-col class="right">
        <h2 class="font-weight-bold font-italic">Database Design</h2>
        <img class="img-fluid img" src="../assets/wallet1.svg" alt="Wallet" />
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import validator from "email-validator";
import pvalidator from "password-validator";
export default {
  name: "Register",
  data() {
    return {
      user: {
        firstName: "",
        lastName: "",
        password: "",
        confirm: "",
        email: "",
      },
    };
  },
  methods: {
    async register() {
      if (
        this.user.email == "" ||
        this.user.password == "" ||
        this.user.firstName == "" ||
        this.user.lastName == ""
      ) {
        alert("Missing required fields");
        return;
      }

      if (!validator.validate(this.user.email)) {
        alert("Invalid email address");
        return;
      }

      var passwordValidator = new pvalidator()
        .is()
        .min(8)
        .is()
        .max(100)
        .has()
        .uppercase() // Must have uppercase letters
        .has()
        .lowercase() // Must have lowercase letters
        .has()
        .digits(2)
        .has()
        .symbols() // Must have at least 2 digits
        .has()
        .not()
        .spaces();

      if (
        !passwordValidator.validate(this.user.password) ||
        this.user.confirm != this.user.password
      ) {
        alert(
          "Password must be a minimum of 8 characters with uppercase letters, lower case letter, digits and at least one special symbol"
        );
        return;
      }
    },
  },
};
</script>

<style lang="scss">
.full-height {
  height: 100vh;
}

.register {
  width: 80%;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -60%);
}
.right {
  background-color: #fff7cb8c;
  height: 100%;
}

.left {
  background-color: white;
  height: 100%;
  text-align: left;
}

.img {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

#login_btn.btn {
  background-color: $primary-color !important;
  border-radius: 50px;
}

#email:focus,
#password:focus,
#first:focus,
#last:focus,
#confirm:focus {
  border-color: $primary-color !important;
}

#email:focus-within,
#password:focus-within,
#confirm:focus-within,
#first:focus-within,
#last:focus-within {
  border-color: $primary-color !important;
  box-shadow: inset 0 0 0 1px $primary-color;
}

.md-form.md-outline input[type="email"]:focus:not([readonly]) + label,
.md-form.md-outline input[type="password"]:focus:not([readonly]) + label,
#first:focus + label,
#confirm:focus + label,
#last:focus + label {
  color: $primary-color !important;
}

.link {
  text-decoration: none;
  color: black;
}

.link:hover {
  text-decoration: none;
}

.forgot_and_register {
  display: flex;
  align-items: center;
}

.forgot_password:hover,
.link:hover {
  color: red;
  transition: color 0.1s ease-in-out;
  cursor: pointer;
}

.third_party {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.fb-logo {
  color: #3b5998;
}

.google-logo {
  color: #db4437;
}

.google-logo:hover,
.fb-logo:hover {
  cursor: pointer;
  box-shadow: 0 3px 9px 0 rgb(0 0 0 / 18%), 0 4px 15px 0 rgb(0 0 0 / 15%);
}
</style>
>

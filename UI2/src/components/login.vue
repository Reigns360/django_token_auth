<template>
  <div>
    <h1>Login Form</h1>
    <form @submit.prevent="login">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password"><br><br>
      <input type="submit" value="Login">
    </form>
    <button @click="logout" v-show="loggedIn">Logout</button>
    <div id="response">{{ message }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      message: "",
      loggedIn: false
    };
  },
  methods: {
    login() {
      const userData = {
        username: this.username,
        password: this.password
      };

      fetch("http://127.0.0.1:8000/api/auth/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(userData)
      })
      .then(response => {
        if (!response.ok) {
          throw new Error("Login failed.");
        }
        return response.json();
      })
      .then(data => {
        localStorage.setItem("token", data.token);
        this.message = "Login successful!";
        this.loggedIn = true;
        // Redirect to next page (you can change this URL)
        this.$router.push("/");
      })
      .catch(error => {
        this.message = "Error: " + error.message;
      });
    },
    logout() {
      fetch("/api/auth/logout/", {
        method: "POST",
        headers: {
          "Authorization": "Token " + localStorage.getItem("token")
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error("Logout failed.");
        }
        return response.json();
      })
      .then(data => {
        localStorage.removeItem("token");
        this.message = "Logout successful!";
        this.loggedIn = false;
      })
      .catch(error => {
        this.message = "Error: " + error.message;
      });
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>

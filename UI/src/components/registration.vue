<template>
  <form @submit.prevent="register">
    <input v-model="username" type="text" placeholder="Username" required>
    <input v-model="email" type="email" placeholder="Email" required>
    <input v-model="password" type="password" placeholder="Password" required>
    <button type="submit">Register</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    async register() {
      // Your registration API call here
    }
  }
};
</script>

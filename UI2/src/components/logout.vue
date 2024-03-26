<template>
  <nav v-if="isLoggedIn">
    <p>Welcome, {{ currentUser.username }}</p>
    <button @click="logout">Logout</button>
  </nav>
  <p v-else>Login to see navigation</p>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    currentUser() {
      return this.$store.getters.currentUser;
    },
  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
    },
  },
};
</script>

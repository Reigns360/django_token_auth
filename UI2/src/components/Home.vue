<template>
  <div>
    <h1>Welcome to Polls voting!</h1>
    <div v-if="isLoggedIn">
      <p>Welcome, {{ currentUser.username }}!</p>
    </div>
    <div v-else>
      <p>Welcome! Please log in to see more.</p>
    </div>
  </div>
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
};
</script>

<style scoped>
</style>

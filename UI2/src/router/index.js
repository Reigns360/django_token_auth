import Vue from 'vue';
import router from 'vue-router';
import login from '@/components/login.vue'; 

Vue.use(router);

export default new router({
  mode: 'history', 
  routes: [
    {
      path: '/',
      redirect: '/login', 
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },
  ],
});

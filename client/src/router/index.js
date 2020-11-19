import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '@/views/Login.vue';
import Contracts from '@/views/Contracts.vue';
import Profile from '@/views/Profile.vue';
import Contract from '@/views/Contract.vue';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/contracts',
    name: 'Contracts',
    component: Contracts,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/contracts/:id',
    name: 'Contract',
    component: Contract,
    meta: {
      requiresAuth: true,
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;

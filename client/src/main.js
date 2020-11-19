import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import Toasted from 'vue-toasted';
import App from './App.vue';
import router from './router';
import store from './store';
import './scss/variables.scss';
import './scss/custom.scss';
import './scss/style.scss';

Vue.use(Toasted, {
  theme: 'toasted-primary',
  position: 'top-center',
  duration: 2000,
});
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');

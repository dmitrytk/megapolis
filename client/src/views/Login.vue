<template>
  <b-container>
    <h1 class="text-center my-3">Login</h1>
    <b-card>
      <b-form  @submit.prevent="onSubmit">
        <b-form-group>
          <b-form-input
            id="input-1"
            v-model="user.username"
            placeholder="Enter username"
            required
            type="text"
          ></b-form-input>
        </b-form-group>

        <b-form-group>
          <b-form-input
            id="input-2"
            v-model="user.password"
            placeholder="Enter password"
            required
            type="password"
          ></b-form-input>
        </b-form-group>
        <b-button class="mr-3" type="submit" variant="primary">Войти</b-button>
        <b-button type="reset" variant="secondary" @click="onCancel">Отмена</b-button>

      </b-form>
    </b-card>
  </b-container>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      user: {
        username: 'executive',
        password: 'Zas322`q',
        message: '',
      },
    };
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/');
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  methods: {
    onSubmit() {
      if (this.user.username && this.user.password) {
        this.$store.dispatch('auth/login', this.user)
          .then(() => {
            this.$router.push('/contracts');
          }, (error) => {
            this.message = (error.response && error.response.data && error.response.data.message)
              || error.message
              || error.toString();
          });
      }
    },
    onCancel() {
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>

</style>

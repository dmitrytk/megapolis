<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand to="/">Megapolis</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/contracts">Договоры</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-button v-if="!this.$store.state.auth.status.loggedIn" class="my-2 my-sm-0"
                  size="sm" to="/login">
          Войти
        </b-button>
        <b-nav-form v-else>
          <b-nav-item to="/profile">
            Привет, {{ this.$store.state.auth.user.first_name }}
          </b-nav-item>
          <b-button class="my-2 my-sm-0" size="sm" @click="logout">Выход</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
  methods: {
    logout() {
      this.$store.dispatch('auth/logout', this.user)
        .then(() => {
          if (this.$route.name !== 'Home') {
            this.$router.push('/');
          }
        }, (err) => {
          this.$toasted.show(`Ошибка\n${err}`);
        });
    },
  },
};
</script>

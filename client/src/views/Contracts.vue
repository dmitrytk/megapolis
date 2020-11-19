<template>
  <b-container>
    <h1 class="text-center my-3">Договоры</h1>
    <b-card>
      <b-list-group v-if="contracts.length">
        <b-list-group-item v-for="contract in contracts"
                           :key="contract.id"
                           :to="{ name: 'Contract', params: { id: contract.id }}"
        >
          {{ contract.number }}
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </b-container>
</template>

<script>
import ContractService from '@/services/contract.service';

export default {
  name: 'Contracts',
  data() {
    return {
      contracts: [],
    };
  },
  mounted() {
    if (this.$store.state.auth.user) {
      this.getContracts();
    } else {
      this.$router.push('/login');
    }
  },
  methods: {
    getContracts() {
      ContractService.getContracts()
        .then((res) => {
          this.contracts = res.data;
        })
        .catch((err) => {
          this.$toasted.show(`Ошибка загрузки данных\n${err}`);
        });
    },
  },
};
</script>

<style scoped>

</style>

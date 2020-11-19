<template>
  <b-container>
    <h1 v-if="contract" class="text-center my-3">Договор № {{ contract.number }}</h1>
    <b-card v-if="employees.length">
      <h3 class="text-center my -2">Работники</h3>
      <b-list-group>
        <b-list-group-item v-for="employee in employees"
                           :key="employee.id">

          {{ employee.first_name }} {{ employee.last_name }}, {{ employee.position }}

          <b-icon-trash type="button" variant="danger"
                        @click="deleteEmployee(employee.id)">
          </b-icon-trash>
        </b-list-group-item>
      </b-list-group>
      <b-button class="mt-3" variant="primary" @click="visible=true">
        Добавить работника
      </b-button>
    </b-card>
    <b-modal
      v-model="visible"
      no-fade
      title="Добавить работника"
      @ok="addEmployee"
    >
      <b-form-select
        v-model="employeeId"
        :options="organizationEmployees">
        <template #first>
          <b-form-select-option :value="null" disabled>
            -- Выберите работника --
          </b-form-select-option>
        </template>
      </b-form-select>
    </b-modal>
  </b-container>
</template>

<script>
import ContractService from '@/services/contract.service';

export default {
  name: 'Contract',
  data() {
    return {
      contract: null,
      employees: [],
      organizationEmployees: [],
      visible: false,
      employeeId: null,
    };
  },
  mounted() {
    this.loadContract();
    this.loadContractEmployees();
    this.loadOrganizationEmployees();
  },
  methods: {
    loadContract() {
      ContractService.getContract(this.$route.params.id)
        .then((res) => {
          this.contract = res.data;
        })
        .catch((err) => {
          this.$toasted.show(`Ошибка загрузки данных\n${err}`);
        });
    },
    loadContractEmployees() {
      ContractService.getContractEmployees(this.$route.params.id)
        .then((res) => {
          this.employees = res.data;
        });
    },
    loadOrganizationEmployees() {
      ContractService.getOrganizationEmployees(this.$store.state.auth.user.organization_id)
        .then((res) => {
          this.organizationEmployees = res.data.map((el) => ({
            text: `${el.first_name} ${el.last_name}`,
            value: el.id,
          }));
        })
        .catch((err) => {
          this.$toasted.show(`Ошибка загрузки всех работников\n${err}`);
        });
    },
    deleteEmployee(employeeId) {
      const employee = this.employees.find((el) => el.id === employeeId);
      if (employee.position !== 'EXECUTIVE') {
        ContractService.deleteEmployee(this.$route.params.id, employeeId)
          .then(() => {
            this.$toasted.show('Работник удален');
            this.loadContractEmployees();
          })
          .catch(() => {
          });
      } else {
        this.$toasted.show('Нельзя удалить гендиректора из договора');
      }
    },
    addEmployee() {
      ContractService.addEmployee(this.$route.params.id, { employee_id: this.employeeId })
        .then(() => {
          this.loadContractEmployees();
        })
        .catch(() => {
          this.$toasted.show('Работник уже в договоре');
        });
    },
  },
};
</script>

<style scoped>

</style>

import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:8000/api';

class ContractService {
  getContracts() {
    return axios.get(`${API_URL}/contracts/`, { headers: authHeader() });
  }

  getContract(id) {
    return axios.get(`${API_URL}/contracts/${id}`, { headers: authHeader() });
  }

  getContractEmployees(id) {
    return axios.get(`${API_URL}/contracts/${id}/employees`, { headers: authHeader() });
  }

  getOrganizationEmployees(id) {
    return axios.get(`${API_URL}/organizations/${id}/employees`, { headers: authHeader() });
  }

  addEmployee(id, data) {
    return axios.post(`${API_URL}/contracts/${id}/employees`, data, { headers: authHeader() });
  }

  deleteEmployee(contractId, employeeId) {
    return axios.delete(`${API_URL}/contracts/${contractId}/employees/${employeeId}`, { headers: authHeader() });
  }
}

export default new ContractService();

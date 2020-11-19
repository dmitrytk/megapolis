import axios from 'axios';

const API_URL = 'http://localhost:8000/api/auth';

class AuthService {
  login(user) {
    return axios
      .post(`${API_URL}/login`, {
        username: user.username,
        password: user.password,
      })
      .then((response) => {
        if (response.data.token) {
          localStorage.setItem('user', JSON.stringify(response.data.user));
          localStorage.setItem('token', JSON.stringify(response.data.token));
        }
        return response.data.user;
      });
  }

  logout() {
    localStorage.removeItem('user');
    localStorage.removeItem('token');
  }
}

export default new AuthService();

// import axios from "axios"

// const tokenString = sessionStorage.getItem('token')//sessionStorage, localStorage //Json Web Token - 
// const baseURL = 'http://localhost:8001/api/'

// const axiosInstance = axios.create({
//   baseURL: "http://127.0.0.1:8000" ,  
//   timeout: 360_000, // 6 mins tbaseURLimeout
//   headers: {
//     'Content-Type': 'application/json',
//     Authorization: Token ${tokenString}
//   },
// })

// export default axiosInstance

import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8001/api/',  
  timeout: 5000,  
  headers: {
    'Content-Type': 'authentication/json',
  },
});


axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;

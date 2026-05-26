import axios from 'axios'

const request = axios.create({
  baseURL: '/api',  // /api/user/login
  timeout: 10000,
})

// 网络请求守卫
request.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')

  if (token) {
    config.headers.Authorization = 'Bearer ' + token
  }

  return config
})

export default request
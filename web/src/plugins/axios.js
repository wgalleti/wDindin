import axios from 'axios'
import constants from '@/constants'

const _axios = axios.create({
  baseURL: 'http://localhost:8000/'
})

_axios.interceptors.request.use((config) => {
  delete config.headers['Authorization']
  const accessToken = localStorage.getItem(constants.TOKEN_KEY_NAME)

  if (accessToken) {
    config.headers['Authorization'] = `Bearer ${accessToken}`
  }

  return config
})

export default _axios

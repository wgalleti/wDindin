import { defineStore } from 'pinia'

import state from '@/store/auth/state'
import getters from '@/store/auth/getters'
import http from '@/plugins/axios'
import constants from '@/constants'

export const useStore = defineStore('auth', {
  state: () => state,
  getters,
  actions: {
    async checkUser() {
      try {
        const { data } = await http.get('/auth/user/')
        localStorage.setItem(constants.USER_DATA_NAME, JSON.stringify(data))
        this.token = localStorage.getItem(constants.TOKEN_KEY_NAME)
        return true
      } catch {
        this.token = null
        this.user = null
        localStorage.removeItem(constants.TOKEN_KEY_NAME)
        localStorage.removeItem(constants.USER_DATA_NAME)
        return false
      }
    },
    async loginUser(credentials) {
      try {
        const { data } = await http.post('/auth/login/', credentials)
        const { token, user } = data
        this.token = token
        this.user = user
        localStorage.setItem(constants.TOKEN_KEY_NAME, token)
        localStorage.setItem(constants.USER_DATA_NAME, JSON.stringify(user))
        return true
      } catch {
        this.token = null
        this.user = null
        localStorage.removeItem(constants.TOKEN_KEY_NAME)
        localStorage.removeItem(constants.USER_DATA_NAME)
        return false
      }
    },
    async logoutUser() {
      try {
        await http.post('/auth/logout/')
      } catch {
        console.log('Faield user logged out')
      }
      localStorage.removeItem(constants.TOKEN_KEY_NAME)
      localStorage.removeItem(constants.USER_DATA_NAME)
      this.token = null
      this.user = null
    },
    setReturnPath(path) {
      this.returnPath = path
    }
  }
})

export default useStore

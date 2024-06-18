import state from '@/store/state.js'
import authStore from '@/store/auth'
import bankStore from '@/store/bank'
import { defineStore } from 'pinia'

export const useStore = defineStore('core', {
  state: () => state,
  actions: {
    setStores() {
      this.auth = authStore()
      this.bank = bankStore()
    }
  }
})

export default useStore

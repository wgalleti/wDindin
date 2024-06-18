import state from '@/store/state.js'
import authStore from '@/store/auth'
import bankStore from '@/store/bank'
import bankAccountStore from '@/store/bankaccount'
import { defineStore } from 'pinia'

export const useStore = defineStore('core', {
  state: () => state,
  actions: {
    setStores() {
      this.auth = authStore()
      this.bank = bankStore()
      this.bankAccount = bankAccountStore()
    }
  }
})

export default useStore

import { defineStore } from 'pinia'
import state from '@/stores/state.js'
import authStore from '@/stores/auth'
import bankStore from '@/stores/bank'
import bankAccountStore from '@/stores/bankaccount'
import categoryStore from '@/stores/category'

export const useStore = defineStore('core', {
  state: () => state,
  actions: {
    setStores() {
      this.auth = authStore()
      this.bank = bankStore()
      this.bankAccount = bankAccountStore()
      this.category = categoryStore()
    }
  }
})

export default useStore

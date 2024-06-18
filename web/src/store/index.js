import { defineStore } from 'pinia'
import state from '@/store/state.js'
import authStore from '@/store/auth'
import bankStore from '@/store/bank'
import bankAccountStore from '@/store/bankaccount'
import categoryStore from '@/store/category'

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

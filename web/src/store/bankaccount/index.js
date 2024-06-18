import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import state from '@/store/bankaccount/state'

export default defineStore('bankAccount', {
  state: () => state,
  actions: {
    async load() {
      try {
        const { data } = await http.get('/api/v1/accounts/', {
          params: { all: true }
        })
        this.banks = data
      } catch {
        this.banks = []
      }
    },
    async loadTypes() {
      try {
        const { data } = await http.get('/api/v1/accounts/types')
        this.types = data
      } catch {
        this.types = []
      }
    },
    async add(bankData) {
      try {
        const { data } = await http.post('api/v1/accounts/', bankData)
        return data
      } catch {
        return false
      }
    },
    async update(key, bankData) {
      try {
        const { data } = await http.put(`api/v1/accounts/${key}`, bankData)
        return data
      } catch {
        return false
      }
    },
    async delete(key) {
      try {
        await http.delete(`api/v1/accounts/${key}`)
        return true
      } catch {
        return false
      }
    }
  }
})

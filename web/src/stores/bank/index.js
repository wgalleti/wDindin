import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import state from '@/stores/bank/state'

export default defineStore('bank', {
  state: () => state,
  actions: {
    async load() {
      try {
        const { data } = await http.get('/api/v1/banks/', {
          params: { all: true }
        })
        this.banks = data
      } catch {
        this.banks = []
      }
    },
    async add(bankData) {
      try {
        const { data } = await http.post('api/v1/banks/', bankData)
        return data
      } catch {
        return false
      }
    },
    async update(key, bankData) {
      try {
        const { data } = await http.put(`api/v1/banks/${key}`, bankData)
        return data
      } catch {
        return false
      }
    },
    async delete(key) {
      try {
        await http.delete(`api/v1/banks/${key}`)
        return true
      } catch {
        return false
      }
    }
  }
})

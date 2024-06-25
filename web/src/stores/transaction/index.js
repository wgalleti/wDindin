import { defineStore } from 'pinia'
import state from '@/stores/transaction/state'
import http from '@/plugins/axios'

export default defineStore('transaction', {
  state: () => state,
  actions: {
    async load() {
      try {
        const { data } = await http.get('/api/v1/transactions/', {
          params: { all: true }
        })
        this.transactions = data
      } catch {
        this.transactions = []
      }
    },
    async add(obj) {
      console.log('adding')
      try {
        const { data } = await http.post('api/v1/transactions/', obj)
        return data
      } catch {
        return false
      }
    },
    async update(key, obj) {
      try {
        const { data } = await http.put(`api/v1/transactions/${key}`, obj)
        return data
      } catch {
        return false
      }
    },
    async delete(key) {
      try {
        await http.delete(`api/v1/transactions/${key}`)
        return true
      } catch {
        return false
      }
    }
  }
})

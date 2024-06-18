import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import state from '@/store/bank/state'

export default defineStore('bank', {
  state: () => state,
  actions: {
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

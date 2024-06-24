import { defineStore } from 'pinia'
import state from '@/stores/creditcard/state'
import http from '@/plugins/axios'

export default defineStore('creditCard', {
  state: () => state,
  actions: {
    async load() {
      try {
        const { data } = await http.get('/api/v1/cards/', {
          params: { all: true }
        })
        this.cards = data
      } catch {
        this.cards = []
      }
    },
    async loadFlags() {
      try {
        const { data } = await http.get('/api/v1/cards/flags/')
        this.flags = data
      } catch {
        this.flags = []
      }
    },
    async add(bankData) {
      try {
        const { data } = await http.post('api/v1/cards/', bankData)
        return data
      } catch {
        return false
      }
    },
    async update(key, bankData) {
      try {
        const { data } = await http.put(`api/v1/cards/${key}`, bankData)
        return data
      } catch {
        return false
      }
    },
    async delete(key) {
      try {
        await http.delete(`api/v1/cards/${key}`)
        return true
      } catch {
        return false
      }
    }
  }
})

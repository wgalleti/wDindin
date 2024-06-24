import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import state from '@/stores/category/state'

export default defineStore('category', {
  state: () => state,
  actions: {
    async load() {
      try {
        const { data } = await http.get('/api/v1/categories/', {
          params: { all: true }
        })
        this.banks = data
      } catch {
        this.banks = []
      }
    },
    async loadTypes() {
      try {
        const { data } = await http.get('/api/v1/categories/types')
        this.types = data
      } catch {
        this.types = []
      }
    },
    async add(bankData) {
      try {
        const { data } = await http.post('api/v1/categories/', bankData)
        return data
      } catch {
        return false
      }
    },
    async update(key, bankData) {
      try {
        const { data } = await http.put(`api/v1/categories/${key}`, bankData)
        return data
      } catch {
        return false
      }
    },
    async delete(key) {
      try {
        await http.delete(`api/v1/categories/${key}`)
        return true
      } catch {
        return false
      }
    }
  }
})

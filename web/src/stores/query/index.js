import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import { useToast } from 'vue-toastification'
const toast = useToast()

const transformTransactions = (data) => {
  return data.map((t) => {
    const { credit_card, bank_account, category } = t
    // Credit card transform
    if (credit_card) {
      const { name, final_number, flag, balance, bank } = credit_card
      t['credit_card_name'] = name
      t['credit_card_final_number'] = final_number
      t['credit_card_flag'] = flag
      t['credit_card_balance'] = balance
      t['bank_name'] = bank?.name
      t['bank_code'] = bank?.code
    }
    // Bank account transform
    if (bank_account) {
      const { name, account_number, balance, bank } = bank_account
      t['bank_account_name'] = name
      t['bank_account_account_number'] = account_number
      t['bank_account_balance'] = balance
      t['bank_name'] = bank?.name
      t['bank_code'] = bank?.code
    }
    // Category transform
    if (category) {
      const { name, icon, transaction_type } = category
      t['category_name'] = name
      t['category_icon'] = icon
      t['transaction_type'] = transaction_type
      t['icon'] = transaction_type === 'INCOME' ? 'mdi-arrow-top-right' : 'mdi-arrow-down-right'
      t['icon_color'] = transaction_type === 'INCOME' ? 'green' : 'red'
    }

    return t
  })
}

export default defineStore('query', {
  state: () => ({
    accountTransactions: [],
    creditCardTransactions: [],
    accountBalances: [],
    creditCardBalances: [],
    transactionsFilter: {
      start: null,
      end: null,
      category: null,
      bankAccount: null,
      creditCard: null
    }
  }),
  actions: {
    async loadTransactions() {
      const { start, end, category, type, bankAccountId, creditCardId } = this.transactionsFilter

      try {
        const { data } = http.get('api/v1/transactions/', {
          params: {
            start,
            end,
            category,
            type,
            bankAccountId,
            creditCardId,
            all: true
          }
        })
        this.accountTransactions = transformTransactions(data)
      } catch (e) {
        console.error('Error loading transactions:', e)
        toast.error('Error loading transactions')
      }
    }
  }
})

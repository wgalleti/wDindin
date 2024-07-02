import { defineStore } from 'pinia'
import http from '@/plugins/axios'
import { useToast } from 'vue-toastification'
import { formatNumber } from 'devextreme/localization'
const toast = useToast()

const transformTransactions = (data) => {
  return data.map((t) => {
    const { credit_card, bank_account, category } = t
    // Credit card transform
    if (credit_card) {
      const { name, final_number, flag, balance, bank } = credit_card
      t['is_credit_card'] = true
      t['is_bank_account'] = false
      t['credit_card_name'] = `${name} - ${bank?.name}`
      t['credit_card_final_number'] = final_number
      t['credit_card_flag'] = flag
      t['credit_card_balance'] = balance
      t['bank_name'] = bank?.name
      t['bank_code'] = bank?.code
    }
    // Bank account transform
    if (bank_account) {
      const { name, account_number, balance, bank } = bank_account
      t['is_bank_account'] = true
      t['is_credit_card'] = false
      t['bank_account_name'] = `${name} - ${bank?.name}`
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

    t['value'] = `R$ ${formatNumber(t.value, { type: 'fixedPoint', precision: 2 })}`

    return t
  })
}

export default defineStore('query', {
  state: () => ({
    transactions: [],
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
        const { data } = await http.get('api/v1/transactions/', {
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
        this.transactions = transformTransactions(data)
      } catch (e) {
        console.error('Error loading transactions:', e)
        toast.error('Error loading transactions')
      }
    }
  }
})

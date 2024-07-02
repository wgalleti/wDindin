<script setup>
import { toRef, onMounted, ref, watch } from 'vue'
import { $store } from '@/main'
import { formatDistanceToNowStrict } from 'date-fns'
import { ptBR } from 'date-fns/locale'
const transactions = toRef($store.query, 'transactions')
const searchQuery = ref('')

const loadTransactions = async () => {
  await $store.query.loadTransactions()
}

onMounted(async () => {
  await loadTransactions()
})

watch(searchQuery, (v) => {
  if (v.length > 2) {
    const search = v
    $store.query.setFilter({ search })
    loadTransactions()
  }

  if (v.length === 0) {
    $store.query.setFilter({ search: null })
    loadTransactions()
  }
})
</script>

<template>
  <div class="w-full mt-2">
    <v-toolbar density="compact" flat color="primary" title="Movimentos">
      <v-text-field
        append-inner-icon="mdi-magnify"
        hide-details
        single-line
        v-model="searchQuery"
      ></v-text-field>
    </v-toolbar>

    <v-list lines="two">
      <v-list-item link v-for="transaction in transactions" :key="transaction.id">
        <template v-slot:prepend>
          <div class="mx-3">
            <v-icon :icon="transaction.icon" :color="transaction.icon_color"></v-icon>
          </div>
        </template>
        <v-list-item-title>{{ transaction.description }}</v-list-item-title>
        <v-list-item-subtitle>
          <div class="flex flex-col gap-1">
            <span class="font-weight-bold text-gray-400">{{ transaction.value }}</span>
            <span class="text-gray-400">{{
              transaction.is_bank_account
                ? transaction.bank_account_name
                : transaction.credit_card_name
            }}</span>
          </div>
        </v-list-item-subtitle>
        <template v-slot:append>
          <div class="font-light">
            {{
              formatDistanceToNowStrict(transaction.created_at, {
                locale: ptBR
              })
            }}
          </div>
        </template>
      </v-list-item>
      <v-list-item link v-if="!transactions.length">
        <v-list-item-title>Sem movimentos</v-list-item-title>
      </v-list-item>
    </v-list>
  </div>
</template>

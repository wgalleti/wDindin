<script setup>
import { toRef, onMounted, computed } from 'vue'
import { $store } from '@/main'
import { formatNumber } from 'devextreme/localization'
const accounts = toRef($store.bankAccount, 'accounts')

const accountTransform = computed(() => {
  const icons = {
    CHECKING: 'mdi-card-account-details',
    INVESTMENT: 'mdi-chart-waterfall',
    CASH: 'mdi-cash-multiple'
  }
  return accounts.value.map((account) => ({
    id: account.id,
    name: account.name,
    balance: formatNumber(account.balance, { type: 'fixedPoint', precision: 0 }),
    type: icons[account.account_type],
    typeName: account.account_type,
    bank: account.bank?.name
  }))
})

async function update() {
  await $store.bankAccount.load()
}

onMounted(async () => {
  update()
})
</script>

<template>
  <div class="flex justify-center gap-2 flex-wrap">
    <v-card
      v-for="account in accountTransform"
      :key="account.id"
      class="min-w-[300px] bg-purple-800"
    >
      <v-card-title class="uppercase font-semibold flex items-center justify-between">
        <div class="flex gap-1 items-center flex-1">
          <v-tooltip location="top">
            <template v-slot:activator="{ props }">
              <v-btn icon v-bind="props" variant="text" size="small">
                <v-icon :icon="account.type" />
              </v-btn>
            </template>
            <span>{{ account.typeName }}</span>
          </v-tooltip>
          <div>{{ account.name }}</div>
        </div>

        <TransactionRegister :bank-account="account.id" @close="update" />
      </v-card-title>
      <v-card-text>
        <p class="text-5xl tracking-tighter font-extralight text-center">{{ account.balance }}</p>
      </v-card-text>
    </v-card>
  </div>
</template>

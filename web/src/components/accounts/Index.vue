<script setup>
import { toRef, onMounted, computed } from 'vue'
import { $store } from '@/main'
import { formatNumber } from 'devextreme/localization'
const accounts = toRef($store.bankAccount, 'accounts')

const accountTransform = computed(() => {
  return accounts.value.map((account) => {
    return {
      id: account.id,
      name: `${account.bank?.name} ${account.name}`,
      balance: `R$ ${formatNumber(account.balance, { type: 'fixedPoint', precision: 2 })}`,
      typeName: account.account_type,
      bank: account.bank?.name,
      color: account.bank?.color
    }
  })
})

async function update() {
  await $store.bankAccount.load()
}

onMounted(async () => {
  update()
})
</script>

<template>
  <v-card class="w-full my-2">
    <v-list bg-color="secondary">
      <v-list-subheader class="text-accent uppercase border-b border-accent mb-2"
        >Contas</v-list-subheader
      >

      <v-list-item v-for="(item, i) in accountTransform" :key="i" :value="item" :color="item.color">
        <template v-slot:append>
          <TransactionRegister :bank-account="item.id" @close="update" focus="description" />
        </template>
        <v-list-item-title>{{ item.name }}</v-list-item-title>
        <v-list-item-subtitle>{{ item.balance }}</v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-card>
</template>

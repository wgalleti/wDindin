<script setup>
import { toRef, computed } from 'vue'
import { $store } from '@/main'
import { formatNumber } from 'devextreme/localization'

const cards = toRef($store.creditCard, 'cards')

const cardTransform = computed(() => {
  return cards.value.map((card) => {
    return {
      id: card.id,
      name: `${card.bank?.name} ${card.name}`,
      balance: `R$ ${formatNumber(card.balance, { type: 'fixedPoint', precision: 2 })}`,
      typeName: card.account_type,
      bank: card.bank?.name,
      color: card.bank?.color
    }
  })
})
async function update() {
  await $store.creditCard.load()
}
</script>

<template>
  <v-card color="primary">
    <v-list bg-color="secondary">
      <v-list-subheader class="text-accent uppercase border-b border-accent mb-2"
        >Cartões</v-list-subheader
      >

      <v-list-item v-for="(item, i) in cardTransform" :key="i" :value="item" :color="item.color">
        <template v-slot:append>
          <TransactionRegister :credit-card="item.id" @close="update" focus="description" />
        </template>
        <v-list-item-title>{{ item.name }}</v-list-item-title>
        <v-list-item-subtitle>{{ item.balance }}</v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-card>
</template>

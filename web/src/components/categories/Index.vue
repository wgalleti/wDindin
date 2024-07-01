<script setup>
import { toRef, computed } from 'vue'
import { $store } from '@/main'
import { formatNumber } from 'devextreme/localization'

const categories = toRef($store.category, 'categories')

const categoryTransform = computed(() => {
  return categories.value.map((category) => {
    return {
      id: category.id,
      name: category.name,
      value: `R$ ${formatNumber(category.value, { type: 'fixedPoint', precision: 0 })}`
    }
  })
})
async function update() {
  await $store.creditCard.load()
}
</script>

<template>
  <v-card class="w-full my-2">
    <v-list>
      <v-list-subheader>Categorias</v-list-subheader>

      <v-list-item
        v-for="(item, i) in categoryTransform"
        :key="i"
        :value="item"
        :color="item.color"
      >
        <template v-slot:append>
          <TransactionRegister :category="item.id" @close="update" focus="description" />
        </template>
        <v-list-item-title>{{ item.name }}</v-list-item-title>
        <v-list-item-subtitle>{{ item.value }}</v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-card>
</template>

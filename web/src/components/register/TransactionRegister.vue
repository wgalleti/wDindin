<script setup>
import { ref } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import TransactionForm from '@/components/forms/TransactionForm'

const oppened = ref(false)
const title = ref('Cadastrar uma nova transação')
const icon = ref('mdi-calendar-check')

function hidde() {
  oppened.value = false
}
function show() {
  oppened.value = true
}
</script>

<template>
  <BaseModalRegister
    :title="title"
    :icon="icon"
    @hidde="hidde"
    @show="show"
    :openend="oppened"
    :width="800"
  >
    <template v-slot:activator>
      <v-icon size="large" :icon="icon" />
    </template>
    <template v-slot:form>
      <TransactionForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

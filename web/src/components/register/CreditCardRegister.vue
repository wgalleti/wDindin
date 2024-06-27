<script setup>
import { ref, computed } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import CreditCardForm from '@/components/forms/CreditCardForm'
import { $store } from '@/main'

const oppened = ref(false)
const title = ref('Cadastrar um novo cartão de crédito')
const icon = ref('mdi-card-account-details')
const badge = computed(() => $store.creditCard.cards.length)

function hidde() {
  oppened.value = false
  $store.creditCard.load()
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
      <v-badge color="error" :content="badge">
        <v-icon size="large" :icon="icon" />
      </v-badge>
    </template>
    <template v-slot:form>
      <CreditCardForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

<script setup>
import { ref } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import TransactionForm from '@/components/forms/TransactionForm'
const emit = defineEmits(['close'])
const form = ref(null)
const oppened = ref(false)
const title = ref('Cadastrar uma nova transação')
const icon = ref('mdi-plus')
const props = defineProps({
  bankAccount: { type: String, required: false },
  creditCard: { type: String, required: false },
  category: { type: String, required: false },
  isCreditCard: { type: Boolean, default: false },
  focus: { type: String, required: 'date' }
})

function hidde() {
  oppened.value = false
  emit('close')
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
      <TransactionForm
        :ref="form"
        @close="hidde"
        :bank-account="props.bankAccount"
        :credit-card="props.creditCard"
        :category="props.category"
        :is-credit-card="!!props.creditCard"
        :focus="props.focus"
      />
    </template>
  </BaseModalRegister>
</template>

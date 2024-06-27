<script setup>
import { ref, computed } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import BankAccountForm from '@/components/forms/BankAccountForm.vue'
import { $store } from '@/main'

const oppened = ref(false)
const title = ref('Cadastrar uma nova conta')
const icon = ref('mdi-wallet-outline')
const badge = computed(() => $store.bankAccount.accounts.length)

function hidde() {
  oppened.value = false
  $store.bankAccount.load()
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
      <BankAccountForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

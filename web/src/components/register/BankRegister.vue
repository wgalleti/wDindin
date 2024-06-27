<script setup>
import { ref, computed } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import BankForm from '@/components/forms/BankForm.vue'
import { $store } from '@/main'

const oppened = ref(false)
const title = ref('Cadastrar uma nova conta')
const icon = ref('mdi-wallet-outline')
const badge = computed(() => $store.bank.banks.length)

function hidde() {
  oppened.value = false
  $store.bank.load()
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
    :width="400"
  >
    <template v-slot:activator>
      <v-badge color="error" :content="badge">
        <v-icon size="large" :icon="icon" />
      </v-badge>
    </template>
    <template v-slot:form>
      <BankForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

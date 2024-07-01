<script setup>
import { ref, computed } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import BankAccountForm from '@/components/forms/BankAccountForm.vue'
import { $store } from '@/main'

const emit = defineEmits(['show'])
const oppened = ref(false)
const title = ref('Contas')
const icon = ref('mdi-wallet-outline')
const badge = computed(() => $store.bankAccount.accounts.length)

function hidde() {
  oppened.value = false
  $store.bankAccount.load()
}
function show() {
  oppened.value = true
  emit('show')
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
      <v-list-item @click="show" link>
        <template v-slot:prepend>
          <v-icon :icon="icon"></v-icon>
        </template>
        <v-list-item-title>{{ title }}</v-list-item-title>
        <template v-slot:append>
          <v-badge color="primary" :content="badge" inline />
        </template>
      </v-list-item>
    </template>
    <template v-slot:form>
      <BankAccountForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

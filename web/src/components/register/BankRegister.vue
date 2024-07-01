<script setup>
import { ref, computed } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import BankForm from '@/components/forms/BankForm.vue'
import { $store } from '@/main'
const emit = defineEmits(['show'])

const oppened = ref(false)
const title = ref('Bancos')
const icon = ref('mdi-bank')
const badge = computed(() => $store.bank.banks.length)

function hidde() {
  oppened.value = false
  $store.bank.load()
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
    :width="400"
  >
    <template v-slot:activator>
      <v-list-item @click="show">
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
      <BankForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

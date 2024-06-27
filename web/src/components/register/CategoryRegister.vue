<script setup>
import { ref, computed } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import CategoryForm from '@/components/forms/CategoryForm.vue'
import { $store } from '@/main'

const oppened = ref(false)
const title = ref('Cadastrar uma nova categoria')
const icon = ref('mdi-shape')
const badge = computed(() => $store.category.categories.length)

function hidde() {
  oppened.value = false
  $store.category.load()
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
    :width="500"
  >
    <template v-slot:activator>
      <v-badge color="error" :content="badge">
        <v-icon size="large" :icon="icon" />
      </v-badge>
    </template>
    <template v-slot:form>
      <CategoryForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

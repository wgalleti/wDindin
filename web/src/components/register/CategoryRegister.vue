<script setup>
import { ref, computed } from 'vue'
import BaseModalRegister from '@/components/register/BaseModalRegister.vue'
import CategoryForm from '@/components/forms/CategoryForm.vue'
import { $store } from '@/main'

const emit = defineEmits(['show'])
const oppened = ref(false)
const title = ref('Categorias')
const icon = ref('mdi-shape')
const badge = computed(() => $store.category.categories.length)

function hidde() {
  oppened.value = false
  $store.category.load()
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
    :width="500"
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
      <CategoryForm @close="hidde" />
    </template>
  </BaseModalRegister>
</template>

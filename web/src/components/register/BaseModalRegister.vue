<script setup>
import { toRefs } from 'vue'
const props = defineProps({
  title: String,
  icon: String,
  openend: Boolean,
  width: Number
})
const { title, icon, openend } = toRefs(props)

const emit = defineEmits(['show', 'hidde'])
</script>

<template>
  <v-dialog v-model="openend" :max-width="width || 600" transition="slide-y-transition" persistent>
    <template v-slot:activator>
      <v-btn class="text-none font-weight-regular" variant="text" @click="emit('show')">
        <slot name="activator"></slot>
      </v-btn>
    </template>

    <v-card :prepend-icon="icon" :title="title">
      <template v-slot:append>
        <v-btn icon="mdi-close" variant="text" @click="emit('hidde')"></v-btn>
      </template>
      <v-card-text class="py-5">
        <slot name="form"> </slot>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

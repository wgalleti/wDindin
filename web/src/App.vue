<template>
  <v-app dark>
    <v-main>
      <v-app-bar app v-if="isLogged">
        <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title class="font-light tracking-tighter text-3xl"
          >wDin$Din$</v-app-bar-title
        >
      </v-app-bar>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { toRef } from 'vue'
import { $store } from '@/main'
const isLogged = toRef($store.auth, 'isAuthenticated')
</script>

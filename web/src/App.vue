<template>
  <v-layout>
    <v-app-bar border="b" class="ps-4" density="compact" flat v-if="isLogged">
      <v-app-bar-title>wDinDin</v-app-bar-title>

      <template #append>
        <BankRegister />
        <BankAccountRegister />
        <CategoryRegister />
        <v-btn class="text-none me-2" height="48" icon slim>
          <v-avatar
            color="surface-light"
            image="https://cdn.vuetifyjs.com/images/john.png"
            size="32"
          />

          <v-menu activator="parent">
            <v-list density="compact" nav>
              <v-list-item append-icon="mdi-cogs" link title="Change Theme" @click="toggleTheme" />
              <v-list-item append-icon="mdi-logout" link title="Logout" to="/logout" />
            </v-list>
          </v-menu>
        </v-btn>
      </template>
    </v-app-bar>

    <v-main>
      <div class="pa-4">
        <router-view />
      </div>
    </v-main>
  </v-layout>
</template>

<script setup>
import { toRef } from 'vue'
import { $store } from '@/main'
import { useTheme } from 'vuetify'

import BankRegister from '@/components/register/BankRegister.vue'
import BankAccountRegister from '@/components/register/BankAccountRegister.vue'
import CategoryRegister from '@/components/register/CategoryRegister.vue'

const isLogged = toRef($store.auth, 'isAuthenticated')
const theme = useTheme()

function toggleTheme() {
  theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
}
</script>

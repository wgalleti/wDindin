<template>
  <v-app dark>
    <v-layout class="h-full w-full">
      <v-app-bar flat v-if="isLogged" app color="secondary">
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer" />
        <v-app-bar-title class="text-accent">wDinDin</v-app-bar-title>

        <template #append>
          <v-btn class="text-none me-2" height="48" icon slim>
            <v-avatar
              color="surface-light"
              image="https://avatars.githubusercontent.com/u/2036130?s=400&u=b47d4273184921c0e33e18cc7a2cc54fc36420e3&v=4"
              size="32"
            />

            <v-menu activator="parent">
              <v-list density="compact" nav>
                <v-list-item append-icon="mdi-cogs" link title="Trocar Tema" @click="toggleTheme" />
                <v-list-item append-icon="mdi-logout" link title="Sair" to="/logout" />
              </v-list>
            </v-menu>
          </v-btn>
        </template>
      </v-app-bar>

      <v-navigation-drawer
        v-model="drawer"
        :location="$vuetify.display.mobile ? 'left' : undefined"
        temporary
      >
        <v-list density="compact" nav>
          <v-list-subheader>Cadastros</v-list-subheader>
          <BankRegister @show="drawer = false" />
          <BankAccountRegister @show="drawer = false" />
          <CreditCardRegister @show="drawer = false" />
          <CategoryRegister @show="drawer = false" />
          <v-divider class="my-3" />
          <v-list-subheader>Opções</v-list-subheader>
          <v-list-item append-icon="mdi-cogs" link title="Trocar Tema" @click="toggleTheme" />
          <v-list-item append-icon="mdi-logout" link title="Sair" to="/logout" />
        </v-list>
      </v-navigation-drawer>

      <v-main class="h-full w-full">
        <router-view />
      </v-main>
    </v-layout>
  </v-app>
</template>

<script setup>
import { ref, toRef, watch } from 'vue'
import { $store } from '@/main'
import { useTheme } from 'vuetify'

import BankRegister from '@/components/register/BankRegister.vue'
import CreditCardRegister from '@/components/register/CreditCardRegister.vue'
import BankAccountRegister from '@/components/register/BankAccountRegister.vue'
import CategoryRegister from '@/components/register/CategoryRegister.vue'

const isLogged = toRef($store.auth, 'isAuthenticated')
const theme = useTheme()

function toggleTheme() {
  theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
  drawer.value = false
}

watch(isLogged, (val) => {
  if (val) {
    $store.bank.load()
    $store.bankAccount.load()
    $store.creditCard.load()
    $store.category.load()
  }
})

const drawer = ref(false)
</script>

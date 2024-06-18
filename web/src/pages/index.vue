<template>
  <v-container fluid>
    <v-col class="flex gap-4">
      <BankRegister />
      <BankAccountRegister />
      <CategoryRegister />
    </v-col>
  </v-container>
</template>

<script setup>
import BankRegister from '@/components/register/BankRegister.vue'
import BankAccountRegister from '@/components/register/BankAccountRegister.vue'
import CategoryRegister from '@/components/register/CategoryRegister.vue'
</script>

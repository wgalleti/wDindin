<template>
  <v-container fluid>
    <v-row fluid>
      <v-col cols="12" md="3" lg="2">
        <Accounts />
        <Cards />
        <Categories />
      </v-col>
      <v-col cols="12" md="9" lg="10"> App </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import Accounts from '@/components/accounts/Index.vue'
import Cards from '@/components/cards/Index.vue'
import Categories from '@/components/categories/Index.vue'
</script>

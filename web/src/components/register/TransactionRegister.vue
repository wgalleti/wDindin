<template>
  <v-dialog v-model="dialog" max-width="900" transition="slide-y-transition" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon="mdi-calendar-check"
        variant="text"
        v-bind="activatorProps"
      />
    </template>

    <v-card prepend-icon="mdi-bank" title="Cadastrar uma nova transação">
      <v-card-text class="py-5">
        <TransactionForm @finished="close" @cancel="close" />
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import TransactionForm from '@/components/forms/TransactionForm'

export default {
  components: {
    TransactionForm
  },
  data: () => ({
    dialog: false
  }),
  methods: {
    close() {
      this.dialog = false
    }
  }
}
</script>

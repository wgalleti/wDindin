<template>
  <v-dialog
    v-model="dialog"
    max-width="600"
    transition="slide-y-transition"
    persistent
  >
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon="mdi-wallet-outline"
        variant="text"
        v-bind="activatorProps"
      ></v-btn>
    </template>

    <v-card prepend-icon="mdi-bank" title="Cadastrar uma nova conta">
      <v-card-text class="py-5">
        <BankAccountForm @finished="close" @cancel="close" />
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import BankAccountForm from '@/components/forms/BankAccountForm.vue'

export default {
  components: {
    BankAccountForm
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

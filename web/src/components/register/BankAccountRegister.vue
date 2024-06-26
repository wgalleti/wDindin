<template>
  <v-dialog v-model="dialog" max-width="900" transition="slide-y-transition" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn class="text-none font-weight-regular" variant="text" v-bind="activatorProps">
        <v-badge color="error" :content="$store.bankAccount.accounts.length">
          <v-icon size="x-large">mdi-wallet-outline</v-icon></v-badge
        >
      </v-btn>
    </template>

    <v-card prepend-icon="mdi-wallet-outline" title="Cadastrar uma nova conta">
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
      this.$store.bankAccount.load()
    }
  }
}
</script>

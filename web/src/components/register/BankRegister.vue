<template>
  <v-dialog v-model="dialog" max-width="600" transition="slide-y-transition" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn class="text-none font-weight-regular" variant="text" v-bind="activatorProps">
        <v-badge color="error" :content="$store.bank.banks.length">
          <v-icon size="large">mdi-bank</v-icon></v-badge
        >
      </v-btn>
    </template>

    <v-card prepend-icon="mdi-bank" title="Cadastrar um novo banco">
      <v-card-text class="py-5">
        <BankForm ref="bankForm" @finished="close" @cancel="close" />
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import BankForm from '@/components/forms/BankForm.vue'

export default {
  components: {
    BankForm
  },
  data: () => ({
    dialog: false
  }),
  methods: {
    close() {
      this.dialog = false
      this.$store.bank.load()
    }
  }
}
</script>

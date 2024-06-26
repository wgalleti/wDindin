<template>
  <v-dialog v-model="dialog" max-width="900" transition="slide-y-transition" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn class="text-none font-weight-regular" variant="text" v-bind="activatorProps">
        <v-badge color="error" :content="$store.creditCard.cards.length">
          <v-icon size="large">mdi-card-account-details</v-icon></v-badge
        >
      </v-btn>
    </template>

    <v-card prepend-icon="mdi-card-account-details" title="Cadastrar um novo cartão de crédito">
      <v-card-text class="py-5">
        <CreditCardForm @finished="close" @cancel="close" />
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import CreditCardForm from '@/components/forms/CreditCardForm'

export default {
  components: {
    CreditCardForm
  },
  data: () => ({
    dialog: false
  }),
  methods: {
    close() {
      this.dialog = false
      this.$store.creditCard.load()
    }
  }
}
</script>

<template>
  <v-dialog v-model="dialog" max-width="900" transition="slide-y-transition" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon="mdi-card-account-details"
        variant="text"
        v-bind="activatorProps"
      />
    </template>

    <v-card prepend-icon="mdi-bank" title="Cadastrar um novo cartão de crédito">
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
    }
  }
}
</script>

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
        prepend-icon="mdi-bank"
        text="Banco"
        variant="tonal"
        v-bind="activatorProps"
      ></v-btn>
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
    }
  }
}
</script>

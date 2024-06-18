<template>
  <v-form ref="form" lazy-validation>
    <v-autocomplete
      v-model="form.bank"
      label="Banco"
      :rules="requiredRule"
      item-title="name"
      item-value="id"
      :items="$store.bank.banks"
      focused
      autofocus
      required
      ref="bank"
    />
    <v-text-field
      v-model="form.name"
      label="Nome"
      :rules="requiredRule"
      required
    />
    <v-number-input
      v-model="form.initial_balance"
      :rules="requiredRule"
      required
      label="Saldo inicial"
    />
    <v-autocomplete
      v-model="form.account_type"
      label="Tipo"
      :rules="requiredRule"
      item-title="name"
      item-value="id"
      :items="this.$store.bankAccount.types"
      focused
    />

    <v-alert
      closable
      text="Falha ao salvar a conta."
      type="error"
      variant="tonal"
      class="my-5"
      v-model="error"
    />
    <v-row class="flex p-5">
      <v-btn @click="$emit('cancel')" variant="plain" :loading="loading"
        >Cancelar</v-btn
      >
      <v-spacer />
      <v-btn
        size="large"
        color="primary"
        @click="submit"
        variant="outlined"
        :loading="loading"
        >Salvar</v-btn
      >
    </v-row>
  </v-form>
</template>

<script>
import { useToast } from 'vue-toastification'

const toast = useToast()
export default {
  data: () => ({
    error: false,
    form: {},
    requiredRule: [(v) => !!v || 'Campo obrigatório']
  }),
  methods: {
    async submit() {
      this.loading = true
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        const data = await this.$store.bankAccount.add(this.form)
        if (data) {
          this.$emit('finished')
          toast.success('Conta registrada com sucesso!')
        } else {
          this.error = true
          this.loading = false
          setTimeout(() => {
            this.$refs.bank.focus()
          }, 100)
        }
      }
    }
  },
  mounted() {
    this.$store.bank.load()
    this.$store.bankAccount.loadTypes()
  }
}
</script>

<style lang="scss" scoped></style>

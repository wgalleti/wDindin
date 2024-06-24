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
    <v-text-field v-model="form.name" label="Nome" :rules="requiredRule" required />
    <v-number-input v-model="form.limit" :rules="requiredRule" required label="Limite" />
    <v-number-input
      v-model="form.final_number"
      :rules="lastNumberRule"
      required
      label="Ultimos Digitos"
      counter="4"
      persistent-counter
    />
    <v-text-field
      v-model="form.expiration_date"
      label="Expira em"
      :rules="expirationRule"
      placeholder="MM/YY"
      required
    />
    <v-autocomplete
      v-model="form.flag"
      label="Bandeira"
      :rules="requiredRule"
      item-title="name"
      item-value="id"
      :items="$store.creditCard.flags"
      focused
    />

    <v-alert
      closable
      text="Falha ao salvar o cartão."
      type="error"
      variant="tonal"
      class="my-5"
      v-model="error"
    />
    <v-row class="flex p-5">
      <v-btn @click="$emit('cancel')" variant="plain" :loading="loading">Cancelar</v-btn>
      <v-spacer />
      <v-btn size="large" color="primary" @click="submit" variant="outlined" :loading="loading"
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
    requiredRule: [(v) => !!v || 'Campo obrigatório'],
    lastNumberRule: [
      (v) => !!v || 'Campo obrigatório',
      (v) => v.toString().length === 4 || 'Somente ultimos 4 números'
    ],
    loading: false
  }),
  computed: {
    expirationRule() {
      return [
        (v) => !!v || 'Campo obrigatório',
        (v) => this.isValidExpirationDate(v) || 'Expiração deve seguir o modelo de MM/YY'
      ]
    }
  },
  methods: {
    isValidExpirationDate(value) {
      if (!value || value.length !== 5 || value[2] !== '/') {
        return false
      }
      const [month, year] = value.split('/').map(Number)
      if (isNaN(month) || isNaN(year) || month < 1 || month > 12) {
        return false
      }
      const currentYear = new Date().getFullYear() % 100 // Last two digits of current year
      const currentMonth = new Date().getMonth() + 1
      if (year < currentYear || (year === currentYear && month < currentMonth)) {
        return false
      }
      return true
    },
    async submit() {
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        this.loading = true

        const data = await this.$store.creditCard.add(this.form)
        if (data) {
          this.$emit('finished')
          toast.success('Cartão registrado com sucesso!')
        } else {
          this.error = true
          this.loading = false
          setTimeout(() => {
            this.$refs.bank.focus()
          }, 100)
        }
      }
    },
    async loadData() {
      await this.$store.creditCard.loadFlags()
      await this.$store.bank.load()
    }
  },
  beforeMount() {
    this.loadData()
  }
}
</script>

<style lang="scss" scoped></style>

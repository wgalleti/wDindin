<template>
  <v-form ref="form" lazy-validation>
    <v-text-field
      v-model="name"
      label="Nome"
      :rules="requiredRule"
      focused
      autofocus
      required
      ref="name"
    />
    <v-text-field
      v-model="code"
      label="Código"
      :rules="requiredRule"
      required
    />
    <v-alert
      closable
      text="Falha ao salvar o banco. Verifique se o código é unico ou entre em contato com o suporte"
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
    name: '',
    code: '',
    requiredRule: [(v) => !!v || 'Campo obrigatório']
  }),
  methods: {
    async submit() {
      this.loading = true
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        const bank = {
          name: this.name,
          code: this.code
        }
        const data = await this.$store.bank.add(bank)
        if (data) {
          this.$emit('finished')
          toast.success('Banco registrado com sucesso!')
        } else {
          this.error = true
          this.loading = false
          setTimeout(() => {
            this.$refs.name.focus()
          }, 100)
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped></style>

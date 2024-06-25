<template>
  <v-form ref="form" lazy-validation>
    <v-container>
      <v-row>
        <v-col cols="12" md="8">
          <v-text-field
            v-model="form.name"
            label="Nome"
            :rules="requiredRule"
            focused
            autofocus
            required
            ref="name"
          />
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field v-model="form.code" label="Código" :rules="requiredRule" required />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-alert
            closable
            text="Falha ao salvar o banco. Verifique se o código é unico ou entre em contato com o suporte"
            type="error"
            variant="tonal"
            class="my-5"
            v-model="error"
          />
        </v-col>
      </v-row>
      <v-row class="flex p-5">
        <v-btn @click="$emit('cancel')" variant="plain" :loading="loading">Cancelar</v-btn>
        <v-spacer />
        <v-btn size="large" color="primary" @click="submit" variant="outlined" :loading="loading"
          >Salvar</v-btn
        >
      </v-row>
    </v-container>
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
        const data = await this.$store.bank.add(this.form)
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

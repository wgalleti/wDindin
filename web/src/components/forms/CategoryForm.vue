<template>
  <v-form ref="form" lazy-validation>
    <v-container>
      <v-row>
        <v-col cols="12">
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
        <v-col cols="12" md="6">
          <v-autocomplete
            v-model="form.icon"
            label="Icone"
            :rules="requiredRule"
            :items="icons"
            item-title="name"
            item-value="id"
          >
            <template v-slot:item="{ props, item }">
              <v-list-item v-bind="props" :prepend-icon="item.value" :title="item.title" />
            </template>
          </v-autocomplete>
        </v-col>
        <v-col cols="12" md="6">
          <v-autocomplete
            v-model="form.transaction_type"
            label="Tipo"
            :rules="requiredRule"
            item-title="name"
            item-value="id"
            :items="this.$store.category.types"
            focused
          />
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
import * as mdiIcons from '@mdi/js'

const toast = useToast()
export default {
  data: () => ({
    error: false,
    form: {},
    requiredRule: [(v) => !!v || 'Campo obrigatório'],
    icons: [],
    loading: false
  }),

  methods: {
    loadIcons() {
      this.icons = Object.keys(mdiIcons).map((icon) => {
        const id = icon.replace(/([A-Z])/g, '-$1').toLocaleLowerCase()
        const name = icon.replace('mdi', '').replace(/([A-Z])/g, ' $1')
        return { id, name }
      })
    },
    async submit() {
      this.loading = true
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        const data = await this.$store.category.add(this.form)
        if (data) {
          this.$emit('finished')
          toast.success('Categoria registrada com sucesso!')
        } else {
          this.error = true
          this.loading = false
          setTimeout(() => {
            this.$refs.name.focus()
          }, 100)
        }
      }
    }
  },
  mounted() {
    this.loadIcons()
    this.$store.category.loadTypes()
  }
}
</script>

<style lang="scss" scoped></style>

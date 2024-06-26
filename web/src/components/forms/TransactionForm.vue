<template>
  <v-form ref="form" lazy-validation>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="4">
          <v-date-input
            v-model="date"
            label="Data"
            :rules="requiredRule"
            required
            prepend-icon=""
            :model-value="formatDate"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6" v-if="!isCreditCard">
          <v-autocomplete
            v-model="form.bank_account"
            label="Conta"
            :rules="!isCreditCard ? requiredRule : []"
            item-title="name"
            item-value="id"
            :items="$store.bankAccount.accounts"
            required
          />
        </v-col>
        <v-col cols="12" md="6" v-if="isCreditCard">
          <v-autocomplete
            v-model="form.credit_card"
            label="Cartão"
            :rules="isCreditCard ? requiredRule : []"
            item-title="name"
            item-value="id"
            :items="$store.creditCard.cards"
            required
          />
        </v-col>
        <v-col cols="12" md="3">
          <v-autocomplete
            v-model="form.category"
            label="Categoria"
            :rules="requiredRule"
            item-title="name"
            item-value="id"
            :items="$store.category.categories"
            required
          />
        </v-col>
        <v-col cols="12" md="3">
          <CurrencyField v-model="form.value" :rules="requiredRule" required label="Valor" />
        </v-col>
        <v-col cols="12" md="12">
          <v-textarea v-model="form.description" label="Descrição" :rules="requiredRule" required />
        </v-col>
      </v-row>
      <v-row>
        <v-alert
          closable
          :text="errorMessage"
          type="error"
          variant="tonal"
          class="my-5"
          v-model="error"
        />
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
import CurrencyField from '@/components/CurrencyField.vue'
export default {
  components: {
    CurrencyField
  },
  props: {
    isCreditCard: {
      type: Boolean,
      default: true
    },
    account: {
      type: String,
      default: ''
    },
    creditCard: {
      type: String,
      default: ''
    },
    category: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    form: {},
    date: new Date(),
    error: false,
    errorMessage: 'Falha ao salvar a transação.',
    loading: false,
    requiredRule: [(v) => !!v || 'Campo obrigatório']
  }),
  computed: {
    formatDate() {
      if (this.date) {
        this.form.date = this.date.toISOString().split('T')[0]
      }
      return this.date
    }
  },
  methods: {
    async loadData() {
      await this.$store.bankAccount.load()
      await this.$store.creditCard.load()
      await this.$store.category.load()
    },
    async submit() {
      this.loading = true
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        try {
          const data = await this.$store.transaction.add(this.form)
          if (data) {
            this.$emit('finished')
            toast.success('Transação registrada com sucesso!')
          } else {
            this.error = true
            this.loading = false
          }
        } catch ({ response }) {
          const { data, status } = response
          if (status === 400) {
            const { non_field_errors = [] } = data
            this.errorMessage = non_field_errors.join(' ')
          }

          this.error = true
          this.loading = false
        }
      }
    }
  },
  mounted() {
    this.loadData()

    if (this.account) {
      this.form.bank_account = this.account
    }
    if (this.creditCard) {
      this.form.credit_card = this.creditCard
    }
    if (this.category) {
      this.form.category = this.category
    }
  }
}
</script>

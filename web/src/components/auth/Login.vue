<template>
  <v-form ref="form" lazy-validation>
    <v-text-field
      v-model="email"
      label="Email"
      prepend-inner-icon="mdi-email"
      type="email"
      :rules="emailRules"
      focused
      autofocus
      required
    />
    <v-text-field
      v-model="password"
      label="Senha"
      prepend-inner-icon="mdi-lock"
      type="password"
      :rules="passwordRules"
      required
    />

    <v-alert
      closable
      text="Usuário ou senha incorretos"
      type="error"
      variant="tonal"
      v-model="error"
      class="my-5"
    />
    <v-btn
      block
      size="x-large"
      color="primary"
      variant="plain"
      @click="submit"
      :loading="loading"
    >
      Login
    </v-btn>
  </v-form>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { $store } from '@/main'
const form = ref(null)
const error = ref(false)
const loading = ref(false)
const email = ref('')
const password = ref('')
const router = useRouter()

const emailRules = [
  (v) => !!v || 'Campo obrigatório',
  (v) => /.+@.+/.test(v) || 'E-mail inválido'
]
const passwordRules = [(v) => !!v || 'Senha é obrigatório']

async function submit() {
  const { valid } = await form.value.validate()

  if (valid) {
    const credentials = {
      email: email.value,
      password: password.value
    }
    const isLogged = await $store.auth.loginUser(credentials)
    if (isLogged) {
      router.push('/')
    } else {
      error.value = true
    }
  }
}
</script>

<style lang="scss" scoped></style>

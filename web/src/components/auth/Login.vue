<template>
  <div class="h-full flex justify-center items-center">
    <v-form @submit.prevent="submit" class="h-auto w-full">
      <DxForm v-bind="formConfig" :form-data="formData" />
    </v-form>
  </div>
</template>

<script setup>
import { useToast } from 'vue-toastification'

import DxForm from 'devextreme-vue/form'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { $store } from '@/main'

const toast = useToast()

const formConfig = {
  labelMode: 'floating',
  labelLocation: 'top',
  showColonAfterLabel: false,
  items: [
    {
      dataField: 'email',
      editorType: 'dxTextBox',
      label: {
        text: 'Email'
      },
      validationRules: [{ type: 'required', message: 'Email é brigatório' }]
    },
    {
      dataField: 'password',
      label: {
        text: 'Senha'
      },
      editorType: 'dxTextBox',
      editorOptions: {
        mode: 'password'
      },
      validationRules: [{ type: 'required', message: 'Senha é obrigatório' }]
    },
    {
      itemType: 'button',
      buttonOptions: {
        text: 'Entrar',
        icon: 'user',
        useSubmitBehavior: true,
        elementAttr: {
          class: 'text-xs bg-purple-800'
        }
      }
    }
  ]
}
const formData = ref({})
const router = useRouter()

async function submit() {
  const { email, password } = formData.value
  const credentials = {
    email,
    password
  }
  const isLogged = await $store.auth.loginUser(credentials)
  if (isLogged) {
    router.push('/')
  } else {
    toast.error('Credenciais inválidas')
  }
}
</script>

<style lang="scss" scoped></style>

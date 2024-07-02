<script setup>
import DxForm from 'devextreme-vue/form'

import { ref } from 'vue'
import { useToast } from 'vue-toastification'
import { $store } from '@/main'

const emit = defineEmits(['close'])
const toast = useToast()
const formData = ref({})

const formConfig = {
  labelMode: 'floating',
  labelLocation: 'top',
  showColonAfterLabel: false,
  colCount: 3,
  items: [
    {
      colSpan: 2,
      dataField: 'name',
      editorType: 'dxTextBox',
      label: {
        text: 'Nome'
      },
      validationRules: [{ type: 'required', message: 'Nome é brigatório' }]
    },
    {
      colSpan: 1,
      dataField: 'code',
      editorType: 'dxTextBox',
      label: {
        text: 'Código'
      },
      validationRules: [{ type: 'required', message: 'Código é brigatório' }]
    },
    {
      colSpan: 3,
      itemType: 'button',
      buttonOptions: {
        text: 'Salvar',
        icon: 'check',
        type: 'success',
        useSubmitBehavior: true
      }
    }
  ]
}

async function submit() {
  const { name, code } = formData.value

  const data = await $store.bank.add({ name, code })
  if (data) {
    emit('close')
    toast.success('Banco registrado com sucesso!')
  } else {
    toast.error('Falha ao salvar o banco')
  }
}
</script>

<template>
  <v-form ref="form" lazy-validation @submit.prevent="submit">
    <DxForm v-bind="formConfig" :form-data="formData" />
  </v-form>
</template>

<style lang="scss" scoped></style>

<script setup>
import DxForm from 'devextreme-vue/form'

import { onMounted, ref } from 'vue'
import { $store } from '@/main'
import { useToast } from 'vue-toastification'

const toast = useToast()
const emit = defineEmits(['close'])
const formData = ref({})
const formConfig = ref({})

async function submit() {
  const data = await $store.bankAccount.add(formData.value)
  if (data) {
    emit('close')
    toast.success('Conta registrada com sucesso!')
  } else {
    toast.error('Falha ao registrar a conta!')
  }
}

onMounted(async () => {
  await $store.bank.load()
  await $store.bankAccount.loadTypes()

  const bankId = $store.bank.banks[0]?.id
  const accountType = $store.bankAccount.types[0]?.id

  formData.value = {
    bank: bankId,
    account_type: accountType
  }

  formConfig.value = {
    labelMode: 'floating',
    labelLocation: 'top',
    showColonAfterLabel: false,
    colCount: 5,
    items: [
      {
        colSpan: 3,
        dataField: 'bank',
        editorType: 'dxSelectBox',
        editorOptions: {
          items: $store.bank.banks,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name', 'code']
        },
        label: {
          text: 'Banco'
        },
        validationRules: [{ type: 'required', message: 'Banco é brigatório' }]
      },
      {
        colSpan: 2,
        dataField: 'account_type',
        editorType: 'dxSelectBox',
        editorOptions: {
          items: $store.bankAccount.types,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name']
        },
        label: {
          text: 'Tipo de Conta'
        },
        validationRules: [{ type: 'required', message: 'Tipo da conta é brigatório' }]
      },
      {
        colSpan: 4,
        dataField: 'name',
        editorType: 'dxTextBox',
        label: {
          text: 'Nome'
        },
        validationRules: [{ type: 'required', message: 'Nome é brigatório' }]
      },
      {
        colSpan: 1,
        dataField: 'initial_balance',
        editorType: 'dxNumberBox',
        editorOptions: {
          format: {
            type: 'fixedPoint',
            precision: 2
          }
        },
        label: {
          text: 'Saldo Inicial'
        },
        validationRules: [{ type: 'required', message: 'Saldo Inicial é brigatório' }]
      },
      {
        colSpan: 5,
        itemType: 'button',
        buttonOptions: {
          text: 'Salvar',
          icon: 'check',
          useSubmitBehavior: true
        }
      }
    ]
  }
})
</script>
<template>
  <v-form ref="form" lazy-validation @submit.prevent="submit">
    <DxForm v-bind="formConfig" :form-data="formData" />
  </v-form>
</template>

<style lang="scss" scoped></style>

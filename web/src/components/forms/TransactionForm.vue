<script setup>
import DxForm from 'devextreme-vue/form'

import { ref, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import { $store } from '@/main'

const props = defineProps({
  bankAccount: { type: Object, required: false },
  creditCard: { type: Object, required: false },
  category: { type: Object, required: false },
  isCreditCard: { type: Boolean, default: false }
})

const emit = defineEmits(['close'])
const toast = useToast()
const formData = ref({})

const formConfig = ref({})

async function submit() {
  const data = await $store.transaction.add(formData.value)
  if (data) {
    emit('close')
    toast.success('Transação registrada com sucesso!')
  } else {
    toast.error('Falha ao registrar a transação')
  }
}

onMounted(async () => {
  await $store.bankAccount.load()
  await $store.creditCard.load()
  await $store.category.load()

  formConfig.value = {
    labelMode: 'floating',
    labelLocation: 'top',
    showColonAfterLabel: false,
    colCount: 11,
    items: [
      {
        dataField: 'date',
        colSpan: 2,
        label: {
          text: 'Data'
        },
        editorType: 'dxDateBox',
        editorOptions: {
          type: 'date',
          displayFormat: 'dd/MM/yyyy',
          dateSerializationFormat: 'yyyy-MM-dd'
        },
        validationRules: [{ type: 'required', message: 'Data é obrigatória' }]
      },
      {
        dataField: 'description',
        colSpan: 9,
        label: {
          text: 'Descrição'
        },
        validationRules: [{ type: 'required', message: 'Descrição é obrigatória' }]
      },
      {
        dataField: 'bank_account',
        colSpan: 6,
        label: {
          text: 'Conta'
        },
        editorType: 'dxSelectBox',
        editorOptions: {
          items: $store.bankAccount.accounts,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name', 'code'],
          disabled: props.isCreditCard
        },
        validationRules: [{ type: 'required', message: 'Contá é obrigatória' }],
        visible: !props.isCreditCard
      },
      {
        dataField: 'credit_card',
        colSpan: 6,
        label: {
          text: 'Cartão'
        },
        editorType: 'dxSelectBox',
        editorOptions: {
          items: $store.creditCard.cards,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name', 'code'],
          disabled: !props.isCreditCard
        },
        validationRules: [{ type: 'required', message: 'Cartão é obrigatória' }],
        visible: props.isCreditCard
      },
      {
        dataField: 'category',
        colSpan: 3,
        label: {
          text: 'Categoria'
        },
        editorType: 'dxSelectBox',
        editorOptions: {
          items: $store.category.categories,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name', 'code']
        },
        validationRules: [{ type: 'required', message: 'Categoria é obrigatória' }]
      },
      {
        dataField: 'value',
        colSpan: 2,
        label: {
          text: 'Valor'
        },
        editorType: 'dxNumberBox',
        editorOptions: {
          format: {
            type: 'fixedPoint',
            precision: 2
          }
        },
        validationRules: [{ type: 'required', message: 'Valor é obrigatório' }]
      },
      {
        colSpan: 11,
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

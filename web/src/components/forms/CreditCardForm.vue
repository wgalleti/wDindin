<script setup>
import DxForm from 'devextreme-vue/form'

import { ref, onMounted } from 'vue'
import { $store } from '@/main'
import { useToast } from 'vue-toastification'
const toast = useToast()

const emit = defineEmits(['close'])

const formData = ref({})
const formConfig = ref({})

async function submit() {
  const data = await $store.creditCard.add(formData.value)
  if (data) {
    emit('finished')
    toast.success('Cartão registrado com sucesso!')
  } else {
    toast.error('Falha ao registrar o cartão!')
  }
}

onMounted(async () => {
  await $store.bank.load()
  await $store.creditCard.loadFlags()

  const bankId = $store.bank.banks[0]?.id

  formData.value = {
    bank: bankId
  }

  formConfig.value = {
    labelMode: 'floating',
    labelLocation: 'top',
    showColonAfterLabel: false,
    colCount: 4,
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
        validationRules: [{ type: 'required', message: 'Banco é obrigatório' }]
      },
      {
        colSpan: 1,
        dataField: 'flag',
        editorType: 'dxSelectBox',
        editorOptions: {
          items: $store.creditCard.flags,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name', 'code']
        },
        label: {
          text: 'Bandeira'
        },
        validationRules: [{ type: 'required', message: 'Bandeira é obrigatório' }]
      },
      {
        colSpan: 1,
        dataField: 'name',
        editorType: 'dxTextBox',
        label: {
          text: 'Nome'
        },
        validationRules: [{ type: 'required', message: 'Nome é obrigatório' }]
      },
      {
        colSpan: 1,
        dataField: 'final_number',
        editorType: 'dxNumberBox',
        label: {
          text: 'Ultimos digitos'
        },
        validationRules: [{ type: 'required', message: 'Os 4 ultimos digitos são obrigatórios' }]
      },
      {
        colSpan: 1,
        dataField: 'expiration_date',
        editorType: 'dxTextBox',
        editorOptions: {
          mask: '00/00',
          maskRules: {
            0: /[0-9]/
          },
          useMaskedValue: true
        },
        validationRules: [
          { type: 'required', message: 'Mês e ano de expiração são obrigatórios' },
          {
            type: 'custom',
            validationCallback: ({ value }) => {
              const dateParts = value.split('/')
              if (dateParts.length !== 2) {
                return false
              }

              const month = parseInt(dateParts[0], 10)
              const year = parseInt('20' + dateParts[1], 10)
              if (isNaN(month) || isNaN(year) || month < 1 || month > 12) {
                return false
              }

              return true
            },
            message: 'Formato inválido. Infome o mes MM e o ano YY'
          },
          {
            type: 'custom',
            validationCallback: ({ value }) => {
              const dateParts = value.split('/')
              const month = parseInt(dateParts[0], 10)
              const year = parseInt('20' + dateParts[1], 10)
              const now = new Date()
              const currentMonth = now.getMonth() + 1 // Months are 0-based
              const currentYear = now.getFullYear()

              if (year < currentYear || (year === currentYear && month < currentMonth)) {
                return false
              }

              return true
            },
            message: 'Cartão vencido!'
          }
        ],
        label: {
          text: 'Expira Em (MM/YY)'
        }
      },
      {
        colSpan: 1,
        dataField: 'limit',
        editorType: 'dxNumberBox',
        editorOptions: {
          format: {
            type: 'fixedPoint',
            precision: 2
          }
        },
        label: {
          text: 'Limite'
        },
        validationRules: [{ type: 'required', message: 'Limite é brigatório' }]
      },
      {
        colSpan: 4,
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

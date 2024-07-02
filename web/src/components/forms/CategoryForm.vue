<script setup>
import DxForm from 'devextreme-vue/form'
import ArrayStore from 'devextreme/data/array_store'
import DataSource from 'devextreme/data/data_source'
import * as mdiIcons from '@mdi/js'

import { onMounted, ref } from 'vue'
import { $store } from '@/main'
import { useToast } from 'vue-toastification'

const toast = useToast()
const emit = defineEmits(['close'])
const formData = ref({})
const formConfig = ref({})

async function submit() {
  const data = await $store.category.add(formData.value)
  if (data) {
    emit('close')
    toast.success('Categoria registrada com sucesso!')
  } else {
    toast.error('Falha ao registrar a categoria!')
  }
}

function loadIcons() {
  const icons = Object.keys(mdiIcons).map((icon) => {
    const id = icon.replace(/([A-Z])/g, '-$1').toLocaleLowerCase()
    const name = icon.replace('mdi', '').replace(/([A-Z])/g, ' $1')
    return { id, name }
  })

  const store = new ArrayStore({
    data: icons,
    key: 'id'
  })

  return new DataSource({
    sort: 'name',
    pageSize: 10,
    store: store
  })
}

onMounted(async () => {
  const iconDataSource = loadIcons()
  await $store.category.loadTypes()

  formConfig.value = {
    labelMode: 'floating',
    labelLocation: 'top',
    showColonAfterLabel: false,
    colCount: 2,
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
        dataField: 'icon',
        editorType: 'dxSelectBox',
        editorOptions: {
          dataSource: iconDataSource,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name', 'code'],
          paginate: true,
          pageSize: 20,
          virtualModeEnabled: true,
          dropDownOptions: {
            height: 400 // Ajuste conforme necessário
          }
        },
        label: {
          text: 'Icone'
        },
        validationRules: [{ type: 'required', message: 'Icone é brigatório' }]
      },
      {
        colSpan: 1,
        dataField: 'transaction_type',
        editorType: 'dxSelectBox',
        editorOptions: {
          items: $store.category.types,
          displayExpr: 'name',
          valueExpr: 'id',
          searchEnabled: true,
          searchMode: 'contains',
          searchExpression: ['name', 'code']
        },
        label: {
          text: 'Tipo'
        },
        validationRules: [{ type: 'required', message: 'Tipo é brigatório' }]
      },
      {
        colSpan: 2,
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
})
</script>
<template>
  <v-form ref="form" lazy-validation @submit.prevent="submit">
    <DxForm v-bind="formConfig" :form-data="formData" />
  </v-form>
</template>

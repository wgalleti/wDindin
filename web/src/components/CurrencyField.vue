<script setup>
import { useCurrencyInput } from 'vue-currency-input'
import { watch } from 'vue'

const props = defineProps({ modelValue: Number })

const { inputRef, formattedValue, numberValue, setValue } = useCurrencyInput({
  locale: 'pt-BR',
  currency: 'BRL',
  currencyDisplay: 'hidden',
  precision: 2,
  hideCurrencySymbolOnFocus: true,
  hideGroupingSeparatorOnFocus: false,
  hideNegligibleDecimalDigitsOnFocus: false,
  autoDecimalDigits: true,
  useGrouping: true,
  accountingSign: false
})

watch(
  () => props.modelValue,
  (value) => {
    setValue(value)
  }
)
</script>

<template>
  <VTextField v-model="formattedValue" ref="inputRef" />
</template>

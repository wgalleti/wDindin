import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

import { createVuetify } from 'vuetify'
import { VNumberInput } from 'vuetify/labs/VNumberInput'
import { VDateInput } from 'vuetify/labs/VDateInput'
import { pt } from 'vuetify/locale'

const wTheme = {
  dark: true,
  colors: {
    primary: '#9adc70',
    secondary: '#2c2d3f',
    error: '#B00020',
    info: '#0068f7',
    success: '#9adc70',
    warning: '#ffb62b'
  }
}

export default createVuetify({
  locale: {
    locale: 'pt',
    fallback: 'pt',
    messages: { pt }
  },
  date: {
    locale: {
      pt: 'pt-BR'
    }
  },
  theme: {
    defaultTheme: 'wTheme',
    themes: {
      wTheme
    }
  },

  components: {
    VNumberInput,
    VDateInput
  }
})

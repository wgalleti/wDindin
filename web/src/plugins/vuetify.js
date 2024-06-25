import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

import { createVuetify } from 'vuetify'
import { VNumberInput } from 'vuetify/labs/VNumberInput'
import { VDateInput } from 'vuetify/labs/VDateInput'
import { pt } from 'vuetify/locale'

const wTheme = {
  dark: true,
  colors: {
    primary: '#6200EE',
    'primary-darken-1': '#3700B3',
    secondary: '#03DAC6',
    'secondary-darken-1': '#018786',
    error: '#B00020',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00'
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

/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

import toastConfig from '@/plugins/toast'
import '@/plugins/axios'

export function registerPlugins(app) {
  app.use(vuetify).use(Toast, toastConfig)
}

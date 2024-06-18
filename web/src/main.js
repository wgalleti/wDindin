/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'
import { createPinia } from 'pinia'

import store from '@/store'
// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const app = createApp(App)
const pinia = createPinia()

registerPlugins(app)
app.use(pinia)

const $store = store()
app.config.globalProperties.$store = $store
app.config.globalProperties.$store.setStores()

app.mount('#app')
export { $store }

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { registerPlugins } from '@/plugins'

import store from '@/stores'
import App from '@/App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

registerPlugins(app)

const $store = store()
app.config.globalProperties.$store = $store
app.config.globalProperties.$store.setStores()
app.mount('#app')

export { $store }

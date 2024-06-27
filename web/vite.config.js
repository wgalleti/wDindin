import { fileURLToPath, URL } from 'node:url'
import { resolve } from 'path'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import Vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
import VueRouter from 'unplugin-vue-router/vite'
import ViteFonts from 'unplugin-fonts/vite'
import Components from 'unplugin-vue-components/vite'
import path from 'node:path'

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    commonjsOptions: {
      esmExternals: true
    },
    lib: {
      entry: resolve(__dirname, './src/main.js'),
      name: 'DevExtreme Vue Bundle',
      formats: ['es', 'cjs'],
      fileName: 'devextreme-vue-bundle'
    },
    rollupOptions: {
      external: ['vue'],
      output: {
        globals: {
          vue: 'Vue'
        }
      }
    },
    outDir: 'devextreme-bundle'
  },
  plugins: [
    vue({
      template: { transformAssetUrls }
    }),
    vueDevTools(),
    Vuetify({
      autoImport: true,
      styles: {
        configFile: 'src/assets/scss/settings.scss'
      }
    }),
    VueRouter(),
    Components(),
    ViteFonts({
      google: {
        families: [
          {
            name: 'Roboto',
            styles: 'wght@100;300;400;500;700;900'
          }
        ]
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      globalize$: path.resolve(__dirname, 'node_modules/globalize/dist/globalize.js'),
      globalize: path.resolve(__dirname, 'node_modules/globalize/dist/globalize'),
      cldr$: path.resolve(__dirname, 'node_modules/cldrjs/dist/cldr.js'),
      cldr: path.resolve(__dirname, 'node_modules/cldrjs/dist/cldr')
    },
    extensions: ['.js', '.vue']
  }
})

import HomeView from '@/pages/index'
import LoginView from '@/pages/login'
import { $store } from '@/main'

export default [
  { path: '/', component: HomeView },
  {
    path: '/login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'Logout',
    async beforeEnter() {
      await $store.auth.logoutUser()
      return '/login'
    }
  }
]

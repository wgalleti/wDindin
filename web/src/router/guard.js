import { $store } from '@/main'

const authGuard = async (to) => {
  const publicPages = ['/login']
  const authRequired = !publicPages.includes(to.path)
  const isAuthenticated = await $store.auth.checkUser()

  if (authRequired && !isAuthenticated) {
    $store.auth.setReturnPath(to.fullPath)
    return '/login'
  }

  if (isAuthenticated) {
    if (to.path == '/login') {
      return '/'
    }
  }
}
export { authGuard }

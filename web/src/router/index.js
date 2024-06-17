import { createRouter, createWebHistory } from 'vue-router/auto'
import { routes } from '@/router/routes'
import { authGuard } from '@/router/guard'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach(authGuard)

export default router

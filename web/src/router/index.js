import { createRouter, createWebHistory } from 'vue-router'

import authGuard from '@/router/guard'
import routes from '@/router/routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach(authGuard)
export default router

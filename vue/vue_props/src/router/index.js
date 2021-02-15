import Vue from 'vue'
import VueRouter from 'vue-router'
import About from '@/views/About.vue'
import Parent from '@/views/Parent.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/parent',
    name: 'Parent',
    component: Parent,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

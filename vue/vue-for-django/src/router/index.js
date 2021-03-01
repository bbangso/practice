import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'

import CreateView from '../views/articles/CreateView.vue'
import ListView from '../views/articles/ListView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/articles/create',
    name: 'CreateView',
    component: CreateView,
    beforeEnter(from, to, next){
      if(Vue.$cookies.isKey('auth-token')){
        next('/LoginView')
      }
      else{
        next()
      }
    }
  },
  {
    path: '/articles/',
    name: 'ListView',
    component: ListView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import LogoutView from '../views/accounts/LogoutView.vue'

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
  },
  {
    path: '/articles/',
    name: 'ListView',
    component: ListView,
  },
  {
    path: '/accounts/logout',
    name: 'LogoutView',
    component: LogoutView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['LoginView', 'Signup', 'Home', 'ListView']  // Login 안해도됨
  const authPages = ['LoginView', 'Signup']  // Login 되어있으면 안됨

  const authRequired = !publicPages.includes(to.name)
  const isLoggedIn = Vue.$cookies.isKey('auth-token')

  const unauthRequired = authPages.includes(to.name)

  if(unauthRequired && isLoggedIn){
    next({ name: 'Home' })
  }

  if(authRequired && !isLoggedIn){
    next({ name: 'LoginView' })
  }
  else{
    next()
  }

})

export default router

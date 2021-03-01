import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'
import router from '@/router'
import axios from 'axios'
import SERVER from '@/api/drf'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    articles: [],
  },
  getters:{
    isLoggedIn(state) {
      return !!state.authToken
    },
    config: state => ({
      headers: {
        Authorization: `Token ${state.authToken}`
      }
    })
  },
  mutations: {
    SET_TOKEN(state, token) {
     state.authToken = token
     cookies.set('auth-token', token) 
    },
    SET_ARTICLES(state, articles){
      state.articles = articles
    }
  },
  actions: {
    postAuthData({ commit }, info){
      axios.post(SERVER.URL + info.location, info.data)
        .then(res =>  {
          commit('SET_TOKEN', res.data.key)
          router.push({ name: 'Home'})
        })
        .catch(err => console.log(err.response))
    },
    signup({ dispatch }, signupData){
      const info = {
        data: signupData,
        location: SERVER.ROUTES.signup
      }
      dispatch('postAuthData', info)
    }, 
    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.login
      }
      dispatch('postAuthData', info)
    },
    logout({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => {
          commit('SET_TOKEN', null)
          cookies.remove('auth-token')
          router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
    },
    fetchArticles({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.articleList)
        .then(res => {
          commit('SET_ARTICLES', res.data)
        })
        .catch(err => console.log(err))
    },
    createArticle({ getters }, articleData) {
      axios.post(SERVER.URL + SERVER.ROUTES.createArticle, articleData, getters.config)
        .then(() => {
          router.push({name:'ListView'})
        })
        .catch(err => console.log(err.response.data))
    }
  },
  modules: {
    // index.js 한장에 모든것을 담기에는 프로젝트가 큰 경우 불편함이 있다 이 경우
    // modules 의 사용법을 익히자!
  }
})

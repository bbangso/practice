<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |  
      <router-link :to="{ name:'ListView' }">Articles</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'LoginView' }">Login</router-link> | 
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link> | 
      <router-link v-if="isLoggedIn" :to="{ name: 'CreateView' }">New Article</router-link> | 
      <router-link v-if="isLoggedIn" @click.native="logout" to="/logout">Logout</router-link>
      <!-- component는 일반적으로 아래에서 올라오는 이벤트만을 기다린다 native를 붙이면
        기존에 존재하는 이벤트임을 명시하는 것이다 
      -->

    </div>
    <router-view @submit-login-data="login" @submit-signup-data="signup"/>
  </div>
</template>

<script>
import axios from 'axios'
// axios.post(URL, BODY, HEADER)


const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  data() {
    return{
      isLoggedIn: false,
    }
  },
  methods: {
    setCookie(token){
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },
    login (loginData) {
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        .then(res =>  {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home'})
        })
        .catch(err => console.log(err.response))
    },
    logout() {
      const requestHeaders = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/rest-auth/logout/', null, requestHeaders)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({name: 'Home'})
        })
        .catch(err => console.log(err.response.data))
    },
    signup(signupData) {
      axios.post(SERVER_URL + '/rest-auth/registration/', signupData)
        .then(res =>  {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home'})
        })
        .catch(err => console.log(err.response.data))
    },
  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token') 
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

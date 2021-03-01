<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |  
      <router-link :to="{ name:'ListView' }">Articles</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'LoginView' }">Login</router-link> | 
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link> | 
      <router-link v-if="isLoggedIn" :to="{ name: 'CreateView' }">New Article</router-link> | 
      <router-link v-if="isLoggedIn" :to="{ name: 'LogoutView' }">Logout</router-link>
      <!-- component는 일반적으로 아래에서 올라오는 이벤트만을 기다린다 native를 붙이면
        기존에 존재하는 이벤트임을 명시하는 것이다 
      -->

    </div>
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
// axios.post(URL, BODY, HEADER)

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  methods: {

  },
  mounted() {
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

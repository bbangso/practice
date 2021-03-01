<template>
  <div>
    <h1>New Article</h1>
    <div>
      <label for="title">title: </label>
      <input v-model="articleData.title" type="text" id="title">
    </div>
    <div>
      <label for="content">content: </label>
      <textarea v-model="articleData.content" type="text" id="content" cols="30" rows="10"></textarea>
    </div>

    <div>
      <button @click="createArticle">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'CreateView',
  data() {
    return{
      articleData: {
        title: null,
        content: null,
      }
    }
  },
  methods:{
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/articles/create/', this.articleData, config)
        .then((res) => {
          console.log(res.data)
          this.$router.push({name:'ListView'})
        })
        .catch(err => console.log(err.response.data))
    }
  },

  created() {
    if (!this.$cookies.isKey('auth-token')) {
      this.$router.push({ name: 'LoginView' })
    }
  }
}
</script>

<style>

</style>
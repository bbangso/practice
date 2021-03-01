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
      <button @click="createArticle(articleData)">Submit</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

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
    ...mapActions(['createArticle'])
  },

  // created() {
  //   if (!this.$cookies.isKey('auth-token')) {
  //     this.$router.push({ name: 'LoginView' })
  //   }
  // }
}
</script>

<style>

</style>
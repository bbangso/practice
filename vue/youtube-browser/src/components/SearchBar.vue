<template>
  <div class="search-bar">
    <!-- vuex 없었을때 
    <input @keypress.enter="onInput" type="text">
    -->
    <input @keypress.enter="fetchVideos" type="text">
  </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      this.$emit('input-change', event.target.value)
    },
    ...mapMutations([
      'setInputValue',
    ]),
    ...mapActions([
      'fetchVideos',
    ])
  },
}
</script>

<style scoped>
div.search-bar {
  text-align: center;
  margin: 20px;
}

div.search-bar > input {
  width: 75%;
}
</style>
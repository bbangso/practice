<template>
  <div class="search-bar">
    <input @keypress.enter="onInput" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      this.$emit('input-change', event.target.value)
    }
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
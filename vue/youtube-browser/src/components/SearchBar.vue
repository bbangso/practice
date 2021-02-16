<template>
  <div>
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

<style>

</style>
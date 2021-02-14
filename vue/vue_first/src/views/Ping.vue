<template>
  <div>
    <h1>Ping</h1>
    <input @keyup.enter="sendToPong" v-model="inputText" type="text">
  </div>
</template>

<script>
export default {
  name: 'Ping',
  data() {
    return {
      inputText: '',
    }
  },
  methods: {
    sendToPong() {
      this.$router.push({
        name:'Pong',
        query: {
          message: this.inputText
        }
      })
    }
  }
}
</script>

<style>

</style>
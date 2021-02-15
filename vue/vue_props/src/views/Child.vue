<template>
  <div class="child">
    <h2>자식 컴포넌트</h2>
    {{ propFromParent }}
    <button @click="signalToParent">이벤트 시그널</button>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    propFromParent: String,  // 유효성 검사
  },
  methods: {
    signalToParent() {
      this.$emit('signal') // custom event
    }
  }
}
</script>

<style>
  .child {
    border: 3px solid blue;
    margin: 3px;
    padding: 3px;
  }
</style>
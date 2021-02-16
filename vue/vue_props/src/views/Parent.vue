<template>
  <div class="parent">
    <h1>부모 컴포넌트</h1>
    <Child @signal="onSignal" :propFromParent="parentMsg"/>
  </div>
</template>

<script>
import Child from '@/views/Child.vue'

export default {
  name: 'Parent',  // 
  data() {
    return {
      parentMsg: '부모에서 내리는 메시지',
    }
  },
  components: {
    Child, // Child: Child 
  },
  methods: {
    onSignal(sig1, sig2) {
      console.log(sig1, sig2)
    }
  }
}
</script>

<style>
  .parent {
    border: 3px solid red;
    margin: 3px;
    padding: 3px;
  }
</style>
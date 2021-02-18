<template>
  <li @click="onVideoSelect" class="list-group-item video-list-item">
    <img class="me-3" :src="thumbnailUrl"/>
    <div class="media-body">
      {{ video.snippet.title }}
    </div>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods:{
    onVideoSelect () {
      this.$emit('video-select', this.video)
    }
  },
  computed: {
    thumbnailUrl () {
      return this.video.snippet.thumbnails.default.url 
    }
  }
}
</script>

<style scoped>
li.video-list-item{
  display: flex;
  cursor: pointer;
}

li.video-list-item:hover{
  background-color: #eee;
}
.media-body{
  margin: auto 0;
}

</style>
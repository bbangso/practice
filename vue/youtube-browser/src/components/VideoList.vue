<template>
    <ul class="list-group col-lg-4">
      <VideoListItem 
        @video-select="onVideoSelect"
        v-for="video in $store.state.videos" 
        :key="video.etag" 
        :video="video"/>
    </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: "VideoList",
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onVideoSelect(video) {
      this.$emit('video-select', video)
    }
  }
}
</script>

<style>

</style>
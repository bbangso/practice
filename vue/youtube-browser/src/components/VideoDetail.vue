<template>
  <div v-if="selectedVideo" class="col-lg-8 ps-0 mb-3">
    <div class="video-detail">
        <div style="position: relative; height: 0px; padding-bottom:56.25%">
        <iframe
          style="position:absolute; width:100%; height:100%"
          :src="videoUrl" 
          allowfullscreen></iframe>
        </div>
    </div>
    <div class="details">
      <h4>
        {{ selectedVideo.snippet.title}}
      </h4>
      <p>{{ selectedVideo.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "VideoDetail",
  props: {
    selectedVideo: Object,
  },
  computed: {
    videoUrl () {
      return `https://youtube.com/embed/${this.selectedVideo.id.videoId}`
    }
  }
}
</script>


<style scoped>
  div.details {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>
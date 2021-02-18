<template>
  <div v-if="selectedVideo" class="col-lg-8">
    <div class="video-detail">
      <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item" 
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
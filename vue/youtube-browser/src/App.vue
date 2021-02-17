<template>
  <div class="container">
    <SearchBar @input-change="onInputChange"/>
    <VideoList :videos="videos"/>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'


/*
  .env.local 파일에 작성한 변수명이
  서버 최초 실행시에 process.env.변수명 으로 자동 설정된다.
  단, 변수명의 접두사가 VUE_APP_ 이어야 한다.
*/

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
  },
  data () {
    return{
      inputValue: '',
      videos: [],
    }
  },
  methods: {
    onInputChange(inputText) {
      this.inputValue = inputText
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          tpye: 'video',
          q: this.inputValue,
        }
      })
        .then(res => this.videos = res.data.items)
        .catch(err => console.error(err))
    }
  }
}
</script>

<style>

</style>

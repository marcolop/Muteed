<template>
  <div id="app">
    <Navbar/>
    <router-view></router-view>
    <footer-bar></footer-bar>
  </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue'
// import Gallery from '@/components/Gallery.vue
// import css from '@/assets/fonts.css'
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'
import FooterBar from '@/components/FooterBar.vue'
import Servicios from '@/components/Servicios.vue'
import Portafolio from '@/components/Portafolio.vue'

export default {
  mounted () {
    console.log(process.env.API)
  },
  name: 'App',
  components: {
    Navbar,
    FooterBar,
    About,
    Home,
    Servicios,
    Portafolio
  }
}
</script>
<style lang="css" scoped>
/*@import "./assets/fonts.css";*/

body{
 height: 100%;
 overflow-x: hidden;
 font-size: 20px;
 background-color: #EFEFEF;
}
</style>

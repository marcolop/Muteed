<template>
  <div id="app">
    <Navbar/>
    <Home/>
    <Servicios/>
    <router-view></router-view>
    <footer-bar></footer-bar>
  </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue'
// import Gallery from '@/components/Gallery.vue'
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'
import FooterBar from '@/components/FooterBar.vue'
import Servicios from '@/components/Servicios.vue'

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
    Servicios
  }
}
</script>
<style>
body{
 height: 100%;
}
</style>

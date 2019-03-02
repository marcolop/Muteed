<template>
  <div class="home">
     <img class="img-fondo" src="../assets/fondo.png">
  </div>
</template>
<script>
// import Gallery from '@/components/Gallery'
export default {
  name: 'Home',
  data () {
    return {
      images: [
        // {fondo: '../assets/fondo.png'}
      ]
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img-fondo {
  width: 1300px;
  height: 650px;
}
.img-fondo:hover {
  filter: sepia(100%);
  box-shadow:
   1px 1px #0a141b,
   2px 2px #53a7ea,
   3px 3px #53a7ea;
-webkit-transform: translateX(-3px);
transform: translateX(-3px);
}
</style>

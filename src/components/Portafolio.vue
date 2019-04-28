<template>
   <div class="portafolio">
      <img  class="size-image" src="../assets/raul.jpg">
      <div class="portafolio2">
        <img class="size-image" src="../assets/pepe.jpg">
         <h2  class="alineado-texto" v-for="item in items" :key="item.id">{{item.name}}</h2>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Portafolio',
  data () {
    return {
      items: [
        {id: 1, name: 'Raúl Garza', img: '../assets/raul.jpg'},
        {id: 2, name: 'Jose Armenta', img: '../assets/pepe.jgp'}
      ]
    }
  }
}
</script>
<style>
.portafolio-class {
  text-align: center;
  margin-left: 170px;
}
.portafolio2 {
  margin-top: 1px;
  margin-left: 250px;
}
.portafolio {
  display: grid;
  grid-template-columns: repeat(2, 290px 300px);
  grid-template-rows: repeat(2, 290px 270px);
  margin-left: 150px;
  margin-top: 94px;
}
.size-image {
 width: 400px;
 opacity: 0.9;
}
.alineado-texto {
  display: grid;
  grid-template-columns: repeat(2, 180px 350px);
  grid-template-rows: repeat(2, 30px 30%);
  margin-left: -450px;
}
</style>

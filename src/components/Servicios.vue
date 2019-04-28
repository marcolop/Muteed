<template>
  <div class="servicios-description">
      <h1 class="class-servicios">SERVICIOS</h1>
         <div class="grid-layout">
           <h2 v-for="servicio in servicios" :key="servicio.id">{{ servicio.service }}</h2>
        </div>
       <div class="">
        <ul class="grid lista-ordenada">
          <li class="" v-for="item in items" :key="item.id">
             {{ item.name }}
          </li>
       </ul>
    </div>
    <div class="logo-muteed">
      <img class="logo" src="../assets/Grupo 9.png">
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      items: [
        {id: 1, name: 'Diseño Sonoro'},
        {id: 2, name: 'AudioLogos'},
        {id: 3, name: 'Composicion Musical'},
        {id: 4, name: 'Stock Music'},
        {id: 5, name: 'Mezcla en formato estéreo y 5.1'},
        {id: 6, name: 'Mastering'},
        {id: 7, name: 'Locución'},
        {id: 8, name: 'Implementacion de audio'},
        {id: 9, name: 'en productos interactivos'},
        {id: 10, name: 'con WWISE'},
        {id: 11, name: 'Sonido directo'},
        {id: 12, name: 'Edicion de Audio'},
        {id: 13, name: 'Composicion Musical'},
        {id: 14, name: 'Music Supervision'},
        {id: 15, name: 'Master'}
      ],
      servicios: [
        {id: 1, service: 'Publicidad'},
        {id: 2, service: 'VideoJuegos'},
        {id: 3, service: 'Tv-Cine'}
      ]
    }
  }
}
</script>
<style scoped>
 .servicios-description {
    text-align: center;
 }
 .lista-ordenada {
   list-style: none;
   /*margin-right: -1200px;*/
  justify-items: left;
   margin-top: 25px;
 }
.layout {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(3, 70% 100px);
    margin-left: -170px;
}
.grid-layout {
    display: grid;
    grid-template-columns:  repeat(3, 180px 450px);
    grid-gap: 20px;
    margin-left: 200px;
    margin-top: 80px;
}
.publicidad {
  text-align: left
}
.grid {
  display: grid;
  grid-template-columns: repeat(1, 310px 370px 270px);
  grid-template-rows: repeat(1, 1fr 20% 20%);
  margin-left: 195px;
}
.image-size {
  width: 1300px;
  height: 650px;
}
.class-servicios {
  margin-top: 78px;
  margin-left: -40px;
}
.logo {
  margin-left: -650px;
  margin-top: 70px;
}
</style>

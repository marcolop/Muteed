<template>
  <div class="servicios-description">
      <h1 class="">Servicios</h1>
       <h2 class="layout">Publicidad</h2>
       <ul class="list-group">
         <li class="list-group-item layout" v-for="item in items" :key="item.name">
             {{ item.name }}
         </li>
       </ul>
  </div>
</template>
<script>
export default {
  data () {
    return {
      items: [
        {name: 'Diseño Sonoro'},
        {name: 'Audio Logos'},
        {name: ''}
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
 }
.layout {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
}
.cell {
    color: #333;
    border-radius: 3px;
    padding: 20px;
    font-size: 10px;
}
.publicidad {
  text-align: left;
}
</style>

<template>
 <nav class="navbar fixed-top navbar-expand-lg navbar-dark scrolling-navbar">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
     <router-link to="/home"><img class="image-size" src="../assets/muteed.png" href="#"><strong></strong></router-link>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto menu-right">
        <router-link v-for="routes in links" v-bind:key="routes.id" :to="`${routes.page}`"><li class="nav-item">
          <a class="nav-link">{{routes.page}}<span class="sr-only"></span></a>
        </li></router-link>
         <!--<li class="nav-item">
          <a class="nav-link" href="#/about">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#/register">Register</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#/login">Login</a>
        </li>-->
      </ul>
    </div>
  </nav>
</template>
<script>
export default {
  name: 'Navbar',
  data  () {
    return {
      links: [
        {
          id: 0,
          text: 'Inicio',
          page: 'Home'
        },
        {
          id: 1,
          text: 'Servicios',
          page: 'Servicios'
        },
        {
          id: 2,
          text: 'Acerca De',
          page: 'Acerca De'
        },
        {
          id: 3,
          text: 'Portafolio',
          page: 'Portafolio'
        }
        // {
        // id: 4
        //  text: ''
        // page: 'Crea Tu Sonido'
        //  }
      ]
    }
  }
}
</script>
<style>
 .view {
    background: url("")no-repeat center center;
    background-size: cover;
    height: 100%;
}
@media (min-width: 768px) {
    .view {
        overflow: visible;
        margin-top: 70px;
    }
}
.navbar {
    background-color:  black;
    z-index: 1;
}
.navbar-nav{
  position: relative;
  left: 580px;
}
.navbar-dark .navbar-nav .nav-link{
  color: white;
}
.top-nav-collapse {
    background-color: transparent;
}
@media only screen and (max-width: 768px) {
    .navbar {
        background-color: black;
    }
}

html,
body,
header,
.view {
  height: 100%;
}
/*tamaño de la imagen*/
.image-size {
  height: 50px;
  /*margin-top: 15px;*/
  /*margin-top: 16px;*/
}
</style>

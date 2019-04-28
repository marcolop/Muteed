<template>
<div class="color-footer">
<!-- Footer -->
<footer class="page-footer font-small cyan darken-3">
    <!-- Footer Elements -->
    <div class="container">
      <!-- Grid row-->
      <div class="row">
        <!-- Grid column -->
        <div class="col-md-12 py-5">
          <div class="mb-5 flex-center">
            <!-- Facebook -->
            <a class="fb-ic">
              <i class="fab fa-facebook-f fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
            </a>
            <!-- Twitter -->
            <a class="tw-ic">
              <i class="fab fa-twitter fa-lg white-text mr-md-5 mr-3 fa-2x"></i>
            </a>
            <!--Instagram-->
            <a class="ins-ic">
              <i class="fab fa-instagram fa-lg white-text mr-md-5 mr-3 fa-2x"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
    <!-- Copyright -->
    <div class="footer-copyright text-center py-3">© 2019 Copyright:
         <img src="../assets/muteed.png" class="img-size">
      <a href="https://mdbootstrap.com/education/bootstrap/">Muteed.com</a>
    </div>
    <!-- Copyright -->
   </footer>
  </div>
</template>
<script>
export default {
  name: 'FooterBar',
  data () {
    return {
      msg: 'este es un footer cool'
    }
  }
}
</script>
<style>
.img-size {
  margin-top: -135px;
  width: 10px;

}
.footer-copyright {
  color: white;
}
.container {
  width: 100%;
  position: relative;
  margin-top: 550px;
}
.row {
   margin-left: 370px;
}
 a,i {
   color: white;
 }
 .color-footer {
  background-color: black
 }
</style>

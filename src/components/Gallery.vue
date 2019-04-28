<template>
 <div class="container mt-4">
  <div class="row">
    <div v-for="image in images" :key="image.id" class="col-md-3 col-sm-4 col-6"><a href="#" v-on:click="showImage(image)"><img class="img-fluid" v-bind:src="image.thumbnail"/></a></div>
  </div>
</div>
</template>
<script>
export default {
  data () {
    return {
      selectedImage: '',
      message: 'This is a Gallery component',
      images: [
        {id: 1, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img2.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'},
        {id: 2, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img2.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'},
        {id: 3, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img3.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'},
        {id: 4, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img4.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'},
        {id: 5, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img5.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'},
        {id: 6, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img6.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'},
        {id: 7, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img7.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'},
        {id: 8, title: 'Marco Lopez', description: '', thumbnail: 'https://vuejsbook.com/img/vuejs/img8.jpg', imageLink: 'https://vuejsbook.com/img/vuejs/img2.jpg'}
      ]
    }
  },
  methods: {
    showImage: function (image) {
      this.selectedImage = image
    }
  }
}
</script>
<style>
.container {
  margin-top: 450px;
  margin-right:  175px;
}
  img {
   -webkit-box-shadow: 0px 1px 6px 1px rgb(0,0,0,0.2);
   -moz-box-shadow: 0px 1px 6px 1px rgb(0,0,0,0.2);
    box-shadow: 0px 1px 6px 1px rgb(0,0,0,0.2);
    margin-bottom: 30px;
  }
  img:hover {
    filter: gray;
    -webkit-filter: grayscale(1);
  }
</style>

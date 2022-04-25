<template>
<div class="entry"><box id='boxx'>lol</box>
</div>
</template>
<script>
import BOX from './components/BOX.vue'
export default{
  name:'App',
  components:{'box':BOX}
}
</script>
<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
.entry{
  background-image: url("./assets/movie poster 2.jpg");
  width:100vw;
  height:100vh;
  margin:0;
  padding:0;
  z-index: -10;
}
*{
margin: 0;
padding: 0;
}
#boxx{
  height:50vh;
  width:60vw;
  position: absolute;
  top:20vh;
  background-color: rgba(0,0,0,.5);
  color: #fff;
  border-radius: 10px;
  left:20vw;
  border:2px solid white
}
</style>

<template>

  <div id="app">
    <Navbar />
      <router-view /> 
    <Footer />
  </div>

  <!-- 
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
  -->
</template>

<script>
  import Navbar from "@/components/Navbar.vue";
  import Footer from "@/components/Footer.vue";

export default {
  name: "App",
  components: {
    Navbar,
    Footer
  } 
}
</script>

<style>
</style>

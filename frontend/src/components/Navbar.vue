<template>
  <nav class="navbar navbar-expand-md bg-dark navbar-dark text-white">
    <div class="container">
      <router-link to="/" class="navbar-brand">Tech<span class="text-info">Blog</span></router-link>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about" class="nav-link">About</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/addarticle" class="nav-link">Add Article</router-link>
          </li>
        </ul>
      </div>
      
    </div>
  </nav>
</template>

<script>

export default {
  name: "Navbar",

}
</script>

<style>

</style>
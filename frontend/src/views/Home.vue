<template>
  <div class="home">
    <HomeData />
  </div>
</template>

<script>
// @ is an alias to /src
import HomeData from "@/components/HomeData.vue";

export default {
  name: "Home",
  components: {
    HomeData,
  },
};
</script>

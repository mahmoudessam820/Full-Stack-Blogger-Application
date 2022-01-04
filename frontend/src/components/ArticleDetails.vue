<template>
  <div id="details" class="details py-3"> 

    <!-- Start article details -->
    <section class="bg-dark text-light">
      <div class="container">
        <div class="text-center">
          <h2 class="text-info">{{ article.title }}</h2> 
          <span>Published Date: {{ article.date }}</span>
          <p>{{ article.body }}</p>
        </div>
        <button class="btn btn-danger mx-3 mt-3 mb-2" @click=" deleteArticle">Delete</button>
        <router-link
        :to="{name:'articleedit', params: {id: article.id}}"
        class="btn btn-success mx-3 mt-3 mb-2"
        >Edit</router-link>
          
      </div>
    </section>
    <!-- End article details -->

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      article: {},
    }
  },
  props: {
    id: {
      type: [Number, String],
      required: true
    }
  },
  methods: {
    getOneArticleData() {
      const path = `http://localhost:5000/article/${this.id}`;
      axios.get(path)
      .then((response) => {
        this.article = response.data.Article;
        console.log(this.article);
      })
      .catch((error) => {
        console.error(error);
      });
    },
    deleteArticle() {
      const path = `http://localhost:5000/delete/${this.id}`;
      axios.delete(path)
      .then(() => {
        this.$router.push({
          name: 'Home'
        });
      })
      .catch((error) => {
        console.error(error);
      });
    },

  },
  created() {
    this.getOneArticleData();
  }
}
</script>

<style>


</style>
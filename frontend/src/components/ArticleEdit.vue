<template>
  <div class="article-edit py-3">

    <section id="edit" >
      <div class="container">
        <h2 class="text-center py-2">Edit Article</h2>
        
        <form @submit="onSubmit">
          <input 
            type="text" 
            class="form-control mb-1"
            v-model="article.title"
            required
          />

          <textarea 
            rows="10"
            class="form-control"
            v-model="article.body"
            required
          >
          </textarea>

          <button
            class="btn btn-success mt-4"
          >
          Update Article
          </button>
        </form>

      </div>
    </section>

  </div>
</template>

<script>
import axios from "axios";

export default {  
  name: 'Edit-Article',
  data() {
    return {
      article: {},
      title: '', 
      body: '',
    }
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    }
  },
  methods: {
    getOneArticleData() {
      const path = `http://localhost:5000/article/${this.id}`;
      axios.get(path)
      .then((response) => {
        this.article = response.data.Article;
        console.log(this.article.title);
        console.log(this.id);
      })
      .catch((error) => {
        console.error(error);
      });
    },
    editArticle(payload) {
      const path = `http://localhost:5000/update/${this.id}`;
      axios.put(path, payload)
      .then(() => {
        this.$router.push({
          name: 'Home'
        });
      })
      .catch((error) => {
        console.error(error);
      });
    },
    onSubmit(e){
      e.preventDefault();
      const payload = {
        title: this.title = this.article.title,
        body: this.body = this.article.body
      };
      this.editArticle(payload)
      console.log(payload);
    },

  },
  created() {
    this.getOneArticleData();
  },

}
</script>

<style>

</style>
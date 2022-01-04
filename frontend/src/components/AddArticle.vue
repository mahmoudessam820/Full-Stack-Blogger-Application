<template>
  <div class="add py-3">
    
    <!-- Start add article  -->
    <section id="add-article">
      <div class="container">
        <h2 class="text-center py-2">Add New Article</h2>
        <form @submit="onSubmit">

          <input 
            type="text" 
            class="form-control mb-1"
            placeholder="Type Title"
            required
            v-model="articleData.title"
          />

          <textarea 
            rows="10"
            class="form-control"
            placeholder="Type the description"
            required
            v-model="articleData.body"
          >
          </textarea>

          <button
            class="btn btn-success mt-4"
          >
          Publish
          </button>

        </form>


      </div>
    </section>
    <!-- End add article  -->

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Add Article",
  data() {
    return {
      articleData: {
        title: '',
        body: '',
      }
    }
  },
  methods: {
    addArticle(payload) {
      const path = 'http://localhost:5000/new';
      axios.post(path, payload)
      .then(() => {
        this.$router.push({
          name: 'Home'
        });
      })  
      .catch((error) => {
        console.error(error.response);
      });
    },
    onSubmit(e) {
      e.preventDefault();
      const payload = {
        title: this.articleData.title,
        body: this.articleData.body
      };
      this.addArticle(payload);
    }
  },
  created() {
    this.addArticle();
  },

}
</script>

<style>

</style>
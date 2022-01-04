<template>
  <div class="home-data">

    <!-- Start Hero -->
    <section id="hero" class="bg-dark text-light text-center text-md-start py-5">
      <div class="container">

        <div class="d-sm-flex align-items-center justify-content-center">
          <div class="py-3">
            <h1 class="display-5">Tech  <span class="text-info">Article</span></h1>
            <p class="py-1 lead">
              Some quick example text to build on the Tack blog content.
            </p>
            <button class="btn btn-info">
              <router-link to="/addarticle" class="btn btn-info">Get Started</router-link>
            </button>
          </div>
          <img class="d-none d-md-block img-fluid w-50" src="../assets/images/hero-img.svg" alt="hero-img">
        </div>

      </div>
    </section>
    <!-- End Hero -->

    <!-- Start content -->
    <section class="py-5 text-center bg-light">
      <div class="container">
        <div class="row">

          <h2>Content</h2>

          <div class="col-sm-12 col-md-6 col-lg-3 py-3">
            <div class="frameworks">
              <div class="card">
                <img src="../assets/images/frameworks-default.svg" alt="frameworks">
                <span class="h5 text-light">frameworks</span>
              </div>
            </div>
          </div>
          <div class="col-sm-12 col-md-6 col-lg-3 py-3">
            <div class="languages">
              <div class="card">
                <img src="../assets/images/languages-default.svg" alt="languages">
                <span class="h5 text-light">languages</span>
              </div>
            </div>
          </div>

          <div class="col-sm-12 col-md-6 col-lg-3 py-3">
            <div class="techniques">
              <div class="card">
                <img src="../assets/images/techniques-default.svg" alt="techniques">
                <span class="h5 text-light">techniques</span>
              </div>
            </div>
          </div>

          <div class="col-sm-12 col-md-6 col-lg-3 py-3">
            <div class="tooling">
              <div class="card">
                <img src="../assets/images/tooling-default.svg" alt="tooling">
                <span class="h5 text-light">tooling</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
    <!-- End content -->

    <!-- Start articles -->
    <section class="py-5 text-center">
      <div class="container">

        <div class="row">

          <div class="col-sm-12 col-md-4 col-lg-3 py-3" v-for="(article, index) in articles" :key="index">
            <div class="card bg-dark text-light">
              <div class="card-body text-center">
                <h5 class="card-title text-info">{{ article.title }}</h5>
                <h6 class="card-subtitle mb-2 text-muted">{{ article.date }}</h6>
                <button class="btn btn-info">
                  <router-link 
                    :to="{name:'details', params: {id:article.id}}"
                    class="btn btn-info"
                  >
                  Read More
                  </router-link>
                </button>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
    <!-- End articles -->

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeData",
  data() {
    return {
      articles: [],
    }
  },
  methods: {
    getArticles() {
      const path = "http://localhost:5000/articles";
      axios.get(path)
      .then((response) => {
        this.articles = response.data.Articles;
      })
      .catch((error) => {
        console.error(error);
      });
    },

  },
  created() {
    this.getArticles();
  },

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.frameworks {
  background-color: #F34878;
  border-radius: 10px;
}

.frameworks .card {
  background-color: transparent;
  border: none;
}

.frameworks img {
  width: 100px;
  margin: auto;
  padding-top: 3px;
}

.languages {
  background-color: #FDC037;
  border-radius: 10px;
}

.languages .card {
  background-color: transparent;
  border: none;
}

.languages img {
  width: 100px;
  margin: auto;
  padding-top: 3px;
}

.techniques {
  background-color: #2DBAF7;
  border-radius: 10px;
}

.techniques .card {
  background-color: transparent;
  border: none;
}

.techniques img {
  width: 100px;
  margin: auto;
  padding-top: 3px;
}

.tooling {
  background-color: #3ABDA1;
  border-radius: 10px;
}

.tooling .card {
  background-color: transparent;
  border: none;
}

.tooling img {
  width: 100px;
  margin: auto;
  padding-top: 3px;
}


</style>
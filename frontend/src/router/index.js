import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import ArticleDetails from "../components/ArticleDetails.vue";
import AddArticle from "../components/AddArticle.vue";
import ArticleEdit from "../components/ArticleEdit.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/addarticle",
    name: "AddArticle",
    component: AddArticle,
  },
  {
    path: "/details/:id",
    name: "details",
    component: ArticleDetails,
    props: true,
  },
  {
    path: "/edit/:id",
    name: "articleedit",
    component: ArticleEdit,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

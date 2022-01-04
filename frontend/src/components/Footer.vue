<template>
  <!-- Start footer  -->
  <footer id="footer" class="bd-footer py-5 mt-5 bg-dark">
    <div class="container py-5">
      <div class="row">

        <div class="col-lg-3 mb-3">
          <a class="d-inline-flex align-items-center mb-2 link-dark text-decoration-none" href="#" aria-label="Bootstrap">
            <img src="../assets/images/blog.png" alt="logo">
            <span class="fs-5 text-light">Tech<span class="text-info">Blog</span></span>
          </a>
          <ul class="list-unstyled small text-muted">
            <li class="mb-2">Designed and built with all the love in the world by the <a href="https://mr-webdev.blogspot.com/">Mr-Web</a>.</li>
          </ul>
        </div>

        <div class="col-6 col-lg-2 offset-lg-1 mb-3">
          <h5 class="text-light">Frameworks</h5>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="https://vuejs.org/">Vue.js</a></li>
            <li class="mb-2"><a href="https://reactjs.org/">React.js</a></li>
            <li class="mb-2"><a href="https://angular.io/">Angular</a></li>
          </ul>
        </div>

        <div class="col-6 col-lg-2 mb-3">
          <h5 class="text-light">Languages</h5>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="https://www.python.org/">Python</a></li>
            <li class="mb-2"><a href="https://www.w3schools.com/js/default.asp">JavaScript</a></li>
            <li class="mb-2"><a href="https://www.php.net/">PHP</a></li>
            <li class="mb-2"><a href="https://www.w3schools.com/CPP/default.asp">C++</a></li>
          </ul>
        </div>

        <div class="col-6 col-lg-2 mb-3">
          <h5 class="text-light">Techniques</h5>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="https://github.com/twbs/bootstrap">Bootstrap 5</a></li>
            <li class="mb-2"><a href="https://github.com/twbs/bootstrap/tree/v4-dev">Bootstrap 4</a></li>
            <li class="mb-2"><a href="https://github.com/twbs/icons">Icons</a></li>
            <li class="mb-2"><a href="https://github.com/twbs/rfs">RFS</a></li>
            <li class="mb-2"><a href="https://github.com/twbs/bootstrap-npm-starter">npm starter</a></li>
          </ul>
        </div>

        <div class="col-6 col-lg-2 mb-3">
          <h5 class="text-light">Community</h5>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="https://dev.to/">Dev.to</a></li>
            <li class="mb-2"><a href="https://forum.freecodecamp.org/">freecodecamp</a></li>
            <li class="mb-2"><a href="https://slack.com/">Slack</a></li>
            <li class="mb-2"><a href="https://stackoverflow.com">Stack Overflow</a></li>
            <li class="mb-2"><a href="https://github.com/">GitHub</a></li>
          </ul>
        </div>

        <div class="d-flex justify-content-between py-4 my-4 border-top">
          <p class="text-light">&copy; 2021 Mr-Web. All rights reserved.</p>
          <ul class="list-unstyled d-flex">
            <li class="ms-3"><a class="link-dark" href="https://twitter.com/Mahmoud42275"><img src="../assets/images/social/icons8-twitter-50.png" alt="twitter" /></a></li>
            <li class="ms-3"><a class="link-dark" href="https://www.linkedin.com/in/mahmoud-essam-822719149/"><img src="../assets/images/social/icons8-linkedin-64.png" alt="linkedin" /></a></li>
            <li class="ms-3"><a class="link-dark" href="http://www.facebook.com/"><img src="../assets/images/social/icons8-facebook-50.png" alt="facebook" /></a></li>
            <li class="ms-3"><a class="link-dark" href="https://github.com/mahmoudessam820"><img  src="../assets/images/social/icons8-compare-git-40.png" alt="github" /></a></li>
          </ul>
        </div>

      </div>
    </div>
  </footer>
  <!-- End footer  -->
</template>

<script>
export default {
  name: "Footer",
}
</script>

<style scoped>

#footer a {
  text-decoration: none;
}

#footer img {
  width: 40px;
}

</style>
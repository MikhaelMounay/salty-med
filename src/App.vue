<template>
  <transition name="fade" mode="out-in">
    <loading-screen
      v-if="loadingScreenOn"
      :LoadingScreenTime="loadingScreenTime"
    />
  </transition>

  <main class="row g-0">
    <div
      id="nav-container"
      class="col-2 animate__animated animate__faster animate__slideInLeft"
      v-if="navOpen"
    >
      <aside
        id="nav-container-aside"
        class="animate__animated animate__slideInLeft"
        v-if="navOpen"
      >
        <nav>
          <router-link
            to="/"
            @click="
              navOpen && smallScreen ? articleBackdropClicked() : '';
              playLoadingScreen();
            "
          >
            <div class="logo-aside display-3">
              <span>I</span>
              <img src="./assets/imgs/logo_O_part.png" alt="IoT Logo" />
              <span>T</span>
            </div>
          </router-link>
          <h1 class="fs-4">Salty Mediterranean</h1>
          <hr class="my-5" />
          <ul>
            <li :class="$route.path == '/' ? 'active' : ''">
              <router-link
                to="/"
                @click="
                  navOpen && smallScreen ? articleBackdropClicked() : '';
                  playLoadingScreen();
                "
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"
                  />
                </svg>
                Home
              </router-link>
            </li>
            <li :class="$route.path == '/results' ? 'active' : ''">
              <router-link
                to="/results"
                @click="
                  navOpen && smallScreen ? articleBackdropClicked() : '';
                  playLoadingScreen();
                "
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M64 32C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V96c0-35.3-28.7-64-64-64H64zm64 192c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32s-32-14.3-32-32V256c0-17.7 14.3-32 32-32zm64-64c0-17.7 14.3-32 32-32s32 14.3 32 32V352c0 17.7-14.3 32-32 32s-32-14.3-32-32V160zM320 288c17.7 0 32 14.3 32 32v32c0 17.7-14.3 32-32 32s-32-14.3-32-32V320c0-17.7 14.3-32 32-32z"
                  />
                </svg>
                Results
              </router-link>
            </li>
            <li :class="$route.path == '/analysis' ? 'active' : ''">
              <router-link
                to="/analysis"
                @click="
                  navOpen && smallScreen ? articleBackdropClicked() : '';
                  playLoadingScreen();
                "
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M64 64c0-17.7-14.3-32-32-32S0 46.3 0 64V400c0 44.2 35.8 80 80 80H480c17.7 0 32-14.3 32-32s-14.3-32-32-32H80c-8.8 0-16-7.2-16-16V64zm406.6 86.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L320 210.7l-57.4-57.4c-12.5-12.5-32.8-12.5-45.3 0l-112 112c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L240 221.3l57.4 57.4c12.5 12.5 32.8 12.5 45.3 0l128-128z"
                  />
                </svg>
                Analysis
              </router-link>
            </li>
            <li :class="$route.path == '/testing' ? 'active' : ''">
              <router-link
                to="/testing"
                @click="
                  navOpen && smallScreen ? articleBackdropClicked() : '';
                  playLoadingScreen();
                "
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M175 389.4c-9.8 16-15 34.3-15 53.1c-10 3.5-20.8 5.5-32 5.5c-53 0-96-43-96-96V64C14.3 64 0 49.7 0 32S14.3 0 32 0H96h64 64c17.7 0 32 14.3 32 32s-14.3 32-32 32V309.9l-49 79.6zM96 64v96h64V64H96zM352 0H480h32c17.7 0 32 14.3 32 32s-14.3 32-32 32V214.9L629.7 406.2c6.7 10.9 10.3 23.5 10.3 36.4c0 38.3-31.1 69.4-69.4 69.4H261.4c-38.3 0-69.4-31.1-69.4-69.4c0-12.8 3.6-25.4 10.3-36.4L320 214.9V64c-17.7 0-32-14.3-32-32s14.3-32 32-32h32zm32 64V224c0 5.9-1.6 11.7-4.7 16.8L330.5 320h171l-48.8-79.2c-3.1-5-4.7-10.8-4.7-16.8V64H384z"
                  />
                </svg>
                Live Testing
              </router-link>
            </li>
            <li :class="$route.path == '/data' ? 'active' : ''">
              <router-link
                to="/data"
                @click="
                  navOpen && smallScreen ? articleBackdropClicked() : '';
                  playLoadingScreen();
                "
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M352 256c0 22.2-1.2 43.6-3.3 64H163.3c-2.2-20.4-3.3-41.8-3.3-64s1.2-43.6 3.3-64H348.7c2.2 20.4 3.3 41.8 3.3 64zm28.8-64H503.9c5.3 20.5 8.1 41.9 8.1 64s-2.8 43.5-8.1 64H380.8c2.1-20.6 3.2-42 3.2-64s-1.1-43.4-3.2-64zm112.6-32H376.7c-10-63.9-29.8-117.4-55.3-151.6c78.3 20.7 142 77.5 171.9 151.6zm-149.1 0H167.7c6.1-36.4 15.5-68.6 27-94.7c10.5-23.6 22.2-40.7 33.5-51.5C239.4 3.2 248.7 0 256 0s16.6 3.2 27.8 13.8c11.3 10.8 23 27.9 33.5 51.5c11.6 26 21 58.2 27 94.7zm-209 0H18.6C48.6 85.9 112.2 29.1 190.6 8.4C165.1 42.6 145.3 96.1 135.3 160zM8.1 192H131.2c-2.1 20.6-3.2 42-3.2 64s1.1 43.4 3.2 64H8.1C2.8 299.5 0 278.1 0 256s2.8-43.5 8.1-64zM194.7 446.6c-11.6-26-20.9-58.2-27-94.6H344.3c-6.1 36.4-15.5 68.6-27 94.6c-10.5 23.6-22.2 40.7-33.5 51.5C272.6 508.8 263.3 512 256 512s-16.6-3.2-27.8-13.8c-11.3-10.8-23-27.9-33.5-51.5zM135.3 352c10 63.9 29.8 117.4 55.3 151.6C112.2 482.9 48.6 426.1 18.6 352H135.3zm358.1 0c-30 74.1-93.6 130.9-171.9 151.6c25.5-34.2 45.2-87.7 55.3-151.6H493.4z"
                  />
                </svg>
                Real Data
              </router-link>
            </li>
            <li :class="$route.path == '/about' ? 'active' : ''">
              <router-link
                to="/about"
                @click="
                  navOpen && smallScreen ? articleBackdropClicked() : '';
                  playLoadingScreen();
                "
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M184 88c0 30.9-25.1 56-56 56s-56-25.1-56-56s25.1-56 56-56s56 25.1 56 56zM64 245.7C54 256.9 48 271.8 48 288s6 31.1 16 42.3V245.7zm144.4-49.3C178.7 222.7 160 261.2 160 304c0 34.3 12 65.8 32 90.5V416c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V389.2C26.2 371.2 0 332.7 0 288c0-61.9 50.1-112 112-112h32c24 0 46.2 7.5 64.4 20.3zM448 416V394.5c20-24.7 32-56.2 32-90.5c0-42.8-18.7-81.3-48.4-107.7C449.8 183.5 472 176 496 176h32c61.9 0 112 50.1 112 112c0 44.7-26.2 83.2-64 101.2V416c0 17.7-14.3 32-32 32H480c-17.7 0-32-14.3-32-32zM568 88c0 30.9-25.1 56-56 56s-56-25.1-56-56s25.1-56 56-56s56 25.1 56 56zm8 157.7v84.7c10-11.3 16-26.1 16-42.3s-6-31.1-16-42.3zM320 160c-35.3 0-64-28.7-64-64s28.7-64 64-64s64 28.7 64 64s-28.7 64-64 64zM240 304c0 16.2 6 31 16 42.3V261.7c-10 11.3-16 26.1-16 42.3zm144-42.3v84.7c10-11.3 16-26.1 16-42.3s-6-31.1-16-42.3zM448 304c0 44.7-26.2 83.2-64 101.2V448c0 17.7-14.3 32-32 32H288c-17.7 0-32-14.3-32-32V405.2c-37.8-18-64-56.5-64-101.2c0-61.9 50.1-112 112-112h32c61.9 0 112 50.1 112 112z"
                  />
                </svg>
                About
              </router-link>
            </li>
            <div class="indicator"></div>
          </ul>
          <button id="close-aside" @click="toggleNav(true)">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
              <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
              <path
                d="M41.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l192 192c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.3 256 278.6 86.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-192 192z"
              />
            </svg>
          </button>
        </nav>
      </aside>
    </div>
    <div class="col">
      <article
        id="article"
        @click="navOpen && smallScreen ? articleBackdropClicked() : ''"
      >
        <div class="mx-auto">
          <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
              <component :is="Component"></component>
            </transition>
          </router-view>
        </div>
      </article>
    </div>
  </main>
  <button id="open-aside" @click="toggleNav(true)" v-if="!navOpen">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
      <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
      <path
        d="M342.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L274.7 256 105.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
      />
    </svg>
  </button>
</template>

<script>
import LoadingScreen from "@/components/LoadingScreen.vue";

export default {
  components: {
    LoadingScreen,
  },
  data() {
    return {
      navOpen: true,
      toggledByUser: false,
      smallScreen: false,
      loadingScreenOn: true,
      loadingScreenTime: 750,
    };
  },
  methods: {
    toggleNav(byUser = false) {
      let navContainer = document.getElementById("nav-container");
      if (this.navOpen == true) {
        navContainer.classList.add("animate__slideOutLeft");
        setTimeout(() => {
          this.navOpen = !this.navOpen;
          document
            .getElementById("article")
            .classList.remove("small-screen-backdrop");
        }, 230);
      } else {
        this.navOpen = !this.navOpen;
        if (this.smallScreen) {
          document
            .getElementById("article")
            .classList.add("small-screen-backdrop");
        }
      }
      setTimeout(() => {
        this.toggledByUser = byUser;
        window.dispatchEvent(new Event("resize"));
      }, 351);
    },
    autoCloseNav() {
      let vw = Math.max(
        document.documentElement.clientWidth || 0,
        window.innerWidth || 0
      );
      let col_3 = (vw / 12) * 2;
      if (col_3 < 250) {
        this.smallScreen = true;
        if (document.getElementById("nav-container-aside")) {
          document
            .getElementById("nav-container")
            .classList.add("small-screen");
          document
            .getElementById("nav-container-aside")
            .classList.add("small-screen");
        }
        if (this.navOpen == true && this.toggledByUser == false) {
          this.toggleNav();
        }
      } else {
        this.smallScreen = false;
        if (document.getElementById("nav-container-aside")) {
          document
            .getElementById("nav-container")
            .classList.remove("small-screen");
          document
            .getElementById("nav-container-aside")
            .classList.remove("small-screen");
        }
      }
      if (this.navOpen == true && this.smallScreen == false) {
        document
          .getElementById("article")
          .classList.remove("small-screen-backdrop");
      } else if (this.navOpen == true && this.smallScreen == true) {
        document
          .getElementById("article")
          .classList.add("small-screen-backdrop");
      }
    },
    articleBackdropClicked() {
      this.toggleNav(true);
    },
    playLoadingScreen() {
      this.loadingScreenOn = true;
      setTimeout(() => {
        this.loadingScreenOn = false;
      }, this.loadingScreenTime);
    },
  },
  mounted() {
    this.playLoadingScreen();
    let local_autoCloseNav = this.autoCloseNav;
    local_autoCloseNav();
    window.addEventListener(
      "resize",
      () => {
        local_autoCloseNav();
      },
      true
    );
  },
};
</script>

<style lang="scss">
@import "./assets/scss/_variables";
// @import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Inter&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  overflow: hidden;
  background-color: $bg-color !important;
  // color: #ddd !important;
  color: #000 !important;
  min-height: 100vh;
  height: 100vh;
}

#app {
  // font-family: "Poppins", sans-serif;
  font-family: "Inter", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
  a {
    text-decoration: none;
    transition: 0.3s;
    color: darken($color: $main-color, $amount: 10);
    &:hover {
      color: darken($color: $main-color, $amount: 20);
    }
  }
}

main {
  height: 100%;
  position: relative;
  div#nav-container {
    z-index: 10;
    padding-right: 0.5rem;
    &.small-screen {
      padding-right: 0;
      width: 0;
    }
  }
  aside {
    --animate-duration: 0.35s;
    padding: 1rem;
    width: 100%;
    height: 100%;
    text-align: center;
    display: block;
    &.small-screen {
      position: fixed;
      top: 0;
      left: 0;
      width: 90vw;
      min-width: 300px;
      max-width: 400px;
      margin-left: 1rem;
      z-index: 10;
    }
    nav {
      height: 100%;
      background-color: darken($color: $bg-color, $amount: 3);
      box-shadow: 0px 1px 7px black;
      border-radius: 2rem;
      padding: 2rem;
      position: relative;
      .logo-aside {
        color: $logo-aside-color;
        font-family: "Varela Round", sans-serif;
        font-weight: 600;
        margin-bottom: 2rem;
        span:nth-child(1),
        img {
          margin-right: 0.5rem;
        }
        img {
          display: inline;
          width: 3rem;
          padding-bottom: 0.7rem;
        }
      }
      ul {
        list-style: none;
        padding: 0;
        position: relative;
        li {
          margin-top: 1rem;
          border-radius: 5px;
          width: 100%;
          position: relative;
          z-index: 1;
          a {
            text-decoration: none;
            color: black;
            display: inline-block;
            width: 100%;
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            &:hover {
              color: darken($color: $main-color, $amount: 10);
            }
            svg {
              width: 20px;
              margin-right: 10px;
              padding-bottom: 4px;
              fill: currentColor;
            }
          }
          &.active a {
            color: $logo-aside-color !important;
          }
          @for $i from 1 through 6 {
            &:nth-child(#{$i}).active ~ .indicator {
              transform: translateY(calc(56.75px * #{$i - 1}));
            }
          }
        }
        .indicator {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 40px;
          border-radius: 5px;
          background-color: $main-color;
          transition: 0.3s;
          z-index: 0;
        }
      }
    }
  }
  article {
    padding: 3rem;
    transition: 0.2s;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100vh;
    width: 100%;
    position: relative;
    z-index: 0;
    @media (max-width: 991.98px) {
      padding: 1rem;
      padding-bottom: 2.5rem;
    }
    &.small-screen-backdrop {
      overflow: hidden;
      &::after {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgb(0, 0, 0, 0.5);
      }
    }
  }
}

#close-aside,
#open-aside {
  position: absolute;
  bottom: 10vh;
  border: none;
  background-color: darken($color: $bg-color, $amount: 3);
  box-shadow: 0px 1px 4px black;
  padding: 0.5rem;
  border-start-end-radius: 10px;
  border-end-end-radius: 10px;
  transition: 0.2s;
  svg {
    width: 13px;
    fill: black;
  }
}
#close-aside {
  right: 0;
  transform: translateX(95%);
  clip-path: inset(-5px -5px -5px 1px);
  &:hover {
    padding-left: 0.25rem;
  }
}
#open-aside {
  left: 0;
  &:hover {
    padding-left: 0.75rem;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
</style>

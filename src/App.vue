<template>
  <!-- <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
  </nav> -->
  <main class="row gx-5 gy-0">
    <!-- <main id="main"> -->
    <div
      id="nav-container"
      class="col-2 animate__animated animate__faster animate__slideInLeft"
      v-if="nav_open"
    >
      <aside
        id="nav-container"
        class="animate__animated animate__slideInLeft"
        v-if="nav_open"
      >
        <nav>
          <h1 class="fs-4">Salty Mediterranean</h1>
          <hr class="my-5" />
          <ul>
            <li :class="$route.path == '/' ? 'active' : ''">
              <router-link to="/">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"
                  />
                </svg>
                Home
              </router-link>
            </li>
            <li :class="$route.path == '/testing' ? 'active' : ''">
              <router-link to="/testing">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512">
                  <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M175 389.4c-9.8 16-15 34.3-15 53.1c-10 3.5-20.8 5.5-32 5.5c-53 0-96-43-96-96V64C14.3 64 0 49.7 0 32S14.3 0 32 0H96h64 64c17.7 0 32 14.3 32 32s-14.3 32-32 32V309.9l-49 79.6zM96 64v96h64V64H96zM352 0H480h32c17.7 0 32 14.3 32 32s-14.3 32-32 32V214.9L629.7 406.2c6.7 10.9 10.3 23.5 10.3 36.4c0 38.3-31.1 69.4-69.4 69.4H261.4c-38.3 0-69.4-31.1-69.4-69.4c0-12.8 3.6-25.4 10.3-36.4L320 214.9V64c-17.7 0-32-14.3-32-32s14.3-32 32-32h32zm32 64V224c0 5.9-1.6 11.7-4.7 16.8L330.5 320h171l-48.8-79.2c-3.1-5-4.7-10.8-4.7-16.8V64H384z"
                  />
                </svg>
                Testing
              </router-link>
            </li>
            <li :class="$route.path == '/about' ? 'active' : ''">
              <router-link to="/about">
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
          <button id="close-aside" @click="toggleNav">
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
      <article>
        <div class="container mx-auto">
          <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
              <component :is="Component"></component>
            </transition>
          </router-view>
        </div>
      </article>
    </div>
  </main>
  <button id="open-aside" @click="toggleNav" v-if="!nav_open">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
      <!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
      <path
        d="M342.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L274.7 256 105.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
      />
    </svg>
  </button>
</template>

<script>
export default {
  data() {
    return {
      nav_open: true,
      // asideToggled: new Event("asideToggled"),
    };
  },
  methods: {
    toggleNav() {
      let navContainer = document.getElementById("nav-container");
      if (this.nav_open == true) {
        navContainer.classList.add("animate__slideOutLeft");
        setTimeout(() => {
          this.nav_open = !this.nav_open;
          // document.dispatchEvent(this.asideToggled);
        }, 230);
      } else {
        this.nav_open = !this.nav_open;
        // document.dispatchEvent(this.asideToggled);
      }
    },
  },
};
</script>

<style lang="scss">
@import "./assets/scss/_variables";
// @import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Inter&display=swap");

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
  // display: flex;
  position: relative;
  aside {
    --animate-duration: 0.35s;
    padding: 1rem;
    width: 17.5vw;
    min-width: 300px;
    height: 100%;
    text-align: center;
    display: block;
    nav {
      height: 100%;
      background-color: darken($color: $bg-color, $amount: 3);
      box-shadow: 0px 1px 7px black;
      border-radius: 2rem;
      padding: 2rem;
      position: relative;
      ul {
        list-style: none;
        padding: 0;
        position: relative;
        li {
          margin-top: 1rem;
          padding-top: 0.5rem;
          padding-bottom: 0.5rem;
          border-radius: 5px;
          width: 100%;
          position: relative;
          z-index: 1;
          a {
            text-decoration: none;
            color: black;
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
            color: black !important;
          }
          @for $i from 1 through 3 {
            &:nth-child(#{$i}).active ~ .indicator {
              transform: translateY(calc(56px * #{$i - 1}));
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
    overflow-y: scroll;
    height: 99vh;
    width: 100%;
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

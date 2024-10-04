<template>
  <div class="home">
    <div class="logo">
      <span>I</span>
      <img src="../assets/imgs/logo_O_part.png" alt="IoT Logo" />
      <span>T</span>
    </div>
    <h1 class="fw-bold">Salty Mediterranean</h1>
    <p class="subtitle text-muted">IoT & Data Analysis Project</p>
    <div class="row gx-4 gy-4 data-overview">
      <div
        class="col-lg-4 col-12 card-container"
        v-for="card in cards"
        :key="card"
      >
        <div class="inner">
          <p class="title" :style="'color: ' + card.color">{{ card.title }}</p>
          <div class="content">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 384 512"
              v-if="card.arrow"
            >
              <!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
              <path
                d="M6.625 215.5l168-176C179.2 34.7 185.4 32.02 192 32.02s12.84 2.688 17.38 7.438l168 176c9.125 9.594 8.781 24.78-.8125 33.94c-9.5 9.156-24.75 8.812-33.94-.8125L216 115.9V456c0 13.25-10.75 23.1-23.1 23.1S168 469.3 168 456V115.9l-126.6 132.7C32.22 258.2 16.97 258.5 7.438 249.4C-2.156 240.2-2.5 225 6.625 215.5z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 384 512"
              v-else
            >
              <!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
              <path
                d="M377.4 296.6l-168 176C204.8 477.3 198.6 480 192 480s-12.84-2.688-17.38-7.438l-168-176C-2.5 286.1-2.156 271.8 7.438 262.6c9.5-9.156 24.75-8.812 33.94 .8125L168 396.1V56.02c0-13.25 10.75-24.01 23.1-24.01S216 42.77 216 56.02v340.1l126.6-132.7c9.156-9.625 24.41-9.969 33.94-.8125C386.2 271.8 386.5 286.1 377.4 296.6z"
              />
            </svg>
            <span>{{ card.number }}</span>
          </div>
          <span class="units">{{ card.unit }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      cards: {
        1: {
          title: "Carbon Dioxide",
          color: "#936e3f",
          arrow: true,
          number: 420,
          unit: "parts per million (current)",
        },
        2: {
          title: "Global Temperature",
          color: "#af5e56",
          arrow: true,
          number: 1.1,
          unit: "°C (since preindustrial)",
        },
        3: {
          title: "Arctic Sea Ice Minimum Extent",
          color: "#7d93b8",
          arrow: false,
          number: 12.6,
          unit: "percent per decade (since 1979)",
        },
        4: {
          title: "Ice Sheets",
          color: "#7a6ea0",
          arrow: false,
          number: 427,
          unit: "billion metric tons per year",
        },
        5: {
          title: "Sea Level",
          color: "#6b99a8",
          arrow: true,
          number: 4,
          unit: "inches (since January 1993)",
        },
        6: {
          title: "Ocean Warming",
          color: "#407aaa",
          arrow: true,
          number: 337,
          unit: "zettajoules (since 1955)",
        },
      },
    };
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/scss/_variables";

.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .logo {
    color: $logo-aside-color;
    font-family: "Varela Round", sans-serif;
    font-weight: 600;
    font-size: 7rem;
    span:nth-child(1),
    img {
      margin-right: 0.5rem;
    }
    img {
      display: inline;
      width: 4.5rem;
      padding-bottom: 0.7rem;
    }
  }
  .subtitle {
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: bold;
    margin-bottom: 3rem;
  }
  .data-overview {
    width: 100%;
    .card-container {
      height: auto;
      div.inner {
        height: 100%;
        border: 2px solid $logo-aside-color;
        border-radius: 3px;
        padding: 1rem;
        transition: 0.2s;
        box-shadow: 4px 3px 0px $logo-aside-color;
        &:hover {
          box-shadow: 6px 5px 0px $logo-aside-color;
        }
        .title {
          font-size: 1.3rem;
          font-weight: bolder;
        }
        .content {
          display: inline-flex;
          align-items: center;
          width: fit-content;
          svg {
            width: 2.5rem;
            margin-right: 0.6rem;
            display: inline-block;
          }
          span {
            font-size: 3.5rem;
            font-weight: 900;
            letter-spacing: -4px;
            display: inline-block;
          }
        }
        span.units {
          padding-left: 1rem;
          display: inline-block;
        }
      }
    }
  }
}
</style>

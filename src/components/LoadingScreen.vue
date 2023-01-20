<template>
  <div class="loading-screen-container">
    <svg
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      x="0px"
      y="0px"
      style="display: none"
    >
      <symbol id="wave">
        <path
          d="M420,20c21.5-0.4,38.8-2.5,51.1-4.5c13.4-2.2,26.5-5.2,27.3-5.4C514,6.5,518,4.7,528.5,2.7c7.1-1.3,17.9-2.8,31.5-2.7c0,0,0,0,0,0v20H420z"
        ></path>
        <path
          d="M420,20c-21.5-0.4-38.8-2.5-51.1-4.5c-13.4-2.2-26.5-5.2-27.3-5.4C326,6.5,322,4.7,311.5,2.7C304.3,1.4,293.6-0.1,280,0c0,0,0,0,0,0v20H420z"
        ></path>
        <path
          d="M140,20c21.5-0.4,38.8-2.5,51.1-4.5c13.4-2.2,26.5-5.2,27.3-5.4C234,6.5,238,4.7,248.5,2.7c7.1-1.3,17.9-2.8,31.5-2.7c0,0,0,0,0,0v20H140z"
        ></path>
        <path
          d="M140,20c-21.5-0.4-38.8-2.5-51.1-4.5c-13.4-2.2-26.5-5.2-27.3-5.4C46,6.5,42,4.7,31.5,2.7C24.3,1.4,13.6-0.1,0,0c0,0,0,0,0,0l0,20H140z"
        ></path>
      </symbol>
    </svg>
    <div class="span-container">
      <span>I</span>
      <span>T</span>
    </div>
    <div class="box">
      <!-- <div class="percent">
        <div class="percentNum" id="count">0</div>
        <div class="percentB">%</div>
      </div> -->
      <div id="water" class="water">
        <svg viewBox="0 0 560 20" class="water_wave water_wave_back">
          <use xlink:href="#wave"></use>
        </svg>
        <svg viewBox="0 0 560 20" class="water_wave water_wave_front">
          <use xlink:href="#wave"></use>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoadingScreen",
  props: ["LoadingScreenTime"],
  mounted() {
    let water = document.getElementById("water");
    let percent = 0;
    let interval;
    interval = setInterval(function () {
      percent++;
      water.style.transform = "translate(0" + "," + (100 - percent) + "%)";
      if (percent == 100) {
        percent = 0;
        setTimeout(() => {
          water.style.transform = "translate(0" + "," + (100 - percent) + "%)";
        }, 250);
        clearInterval(interval);
      }
    }, (this.LoadingScreenTime - 250) / 100);
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/scss/_variables";
@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

*,
*:before,
*:after {
  box-sizing: border-box;
  outline: none;
}

.loading-screen-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 100;
  background-color: white;
}

.span-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 300px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  span {
    display: inline-block;
    width: 100px;
    color: $boxColor;
    text-align: center;
    font-size: 10rem;
    font-weight: 900;
    font-family: "Varela Round", sans-serif;
    &:nth-child(2) {
      padding-left: 25px;
    }
    @media (max-width: 991.98px) {
      &:nth-child(2) {
        padding-left: 0;
      }
    }
  }
}

.box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 100px;
  width: 100px;
  background: $boxColor;
  border-radius: 100%;
  overflow: hidden;
  .water {
    position: absolute;
    left: 0;
    top: 0;
    z-index: 2;
    width: 100%;
    height: 100%;
    transform: translate(0, 100%);
    background: $waterFColor;
    transition: all 0.3s;
    &_wave {
      width: 200%;
      position: absolute;
      bottom: 100%;
      &_back {
        right: 0;
        fill: $waterBColor;
        animation: wave-back 1.4s infinite linear;
      }
      &_front {
        left: 0;
        fill: $waterFColor;
        margin-bottom: -1px;
        animation: wave-front 0.7s infinite linear;
      }
    }
  }
}
@keyframes wave-front {
  100% {
    transform: translate(-50%, 0);
  }
}

@keyframes wave-back {
  100% {
    transform: translate(50%, 0);
  }
}
</style>

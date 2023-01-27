<template>
  <div class="container">
    <div class="references">
      <a href="https://www.copernicus.eu/">
        <img
          src="../assets/imgs/logo-copernicus.svg"
          alt="Copernicus Logo"
          class="me-3"
        />
      </a>
      <a href="https://marine.copernicus.eu">
        <img
          src="../assets/imgs/Copernicus_Marine_Service_logo.png"
          alt="Copernicus Marine Service Logo"
        />
      </a>
    </div>
    <iframe
      src="https://data.marine.copernicus.eu/viewer/expert?view=viewer&crs=epsg:4326&t=1674302400000&z=0&center=15.150000000000006,38.07999999999999&zoom=10.95035424409248&layers=W3siaWQiOiJjMiIsImxheWVySWQiOiJNRURTRUFfTVVMVElZRUFSX1BIWV8wMDZfMDA0L2NtZW1zX21vZF9tZWRfcGh5LWN1cl9teV80LjJrbV9QMVktbS9zZWFfd2F0ZXJfdmVsb2NpdHkiLCJsb2dTY2FsZSI6ZmFsc2V9XQ=="
      frameborder="0"
    ></iframe>
  </div>
</template>

<script>
export default {
  name: "RealDataView",
};
</script>

<style lang="scss" scoped>
.container {
  height: 85%;
  .references {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 2rem;
    img {
      width: 200px;
      @media (max-width: 991.98px) {
        width: 150px;
      }
    }
  }
  iframe {
    width: 100%;
    height: 550px;
    min-height: 300px;
    padding: 0.15rem;
    resize: vertical;
  }
}
</style>

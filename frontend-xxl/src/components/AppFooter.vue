<template>
  <v-footer class="bg-grey-lighten-1" style="background-color: #495c41; border-top: #cb8764; border-style: solid; border-top-color: #cb8764; border-width: 2px 0 0 0;">
    <v-row justify="center" no-gutters>
      <v-col md="5" xs="12" class="pr-10 my-10 footer-text">
        <v-divider class="my-3" color="#cb8764"></v-divider>
        <h2>Links und Downloads</h2>
        <v-divider class="my-3" color="#cb8764"></v-divider>
        <p><a href="https://zeltlager-braeunlingen.de/impressum/" style="color: #ddd6c4; text-decoration: none;">Impressum</a></p>
        <p><a href="https://zeltlager-braeunlingen.de/datenschutz/" style="color: #ddd6c4; text-decoration: none;">Datenschutzerklärung</a></p>
      </v-col>
      <v-col md="5" xs="12" class="pl-10 my-10 footer-text">
        <v-divider class="my-3" color="#cb8764"></v-divider>
        <h2>Zeltlager Bräunlingen</h2>
        <v-divider class="my-3" color="#cb8764"></v-divider>
        <p>Röm. Kath. Kirchengemeinde Auf der Baar<br>Pfarrbüro Bräunlingen
          <br>Hüfingerstraße 2<br>78199 Bräunlingen</p>
        <p>+49 771  61176<br><a href="mailto:info@zeltlager-braeunlingen.de" style="color: #ddd6c4; text-decoration: none;">info@zeltlager-braeunlingen.de</a></p>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Blog',
        'Contact Us',
      ],
    }),
  }
</script>

<style>

.footer-text {
  color: #ddd6c4 
}


</style>
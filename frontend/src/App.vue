<template>
  <v-app style="background-color: #ddd6c4;">
    <v-app-bar app color="#ddd6c4" >
      <!-- Adjust the height to your needs, mine is 40 -->
      <img :src="require('./assets/logo.png')" height="50"/>
      <v-spacer><h3 style="text-align: right;">Anmeldung Kinderlager</h3></v-spacer>
    </v-app-bar>
    <!--<v-app-bar
      app
      color="#ddd6c4"
      dark
    >
      <div class="align-center">
        <v-img
          alt="shrink Vuetify Logo"
          class="mr-2"
          
          src="./assets/logo.png"
          transition="scale-transition"
          
          width="200"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>-->

    <v-main>
      <Form/>
    </v-main>
    <AppFooter/>
  </v-app>
</template>

<script>
import Form from './components/Form';
import AppFooter from './components/AppFooter';

export default {
  name: 'App',

  components: {
    Form,
    AppFooter
  },

  data: () => ({
    //
  }),
};
</script>

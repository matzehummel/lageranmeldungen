<template>
  <v-app style="background-color: #ddd6c4;">
    <v-app-bar app color="#ddd6c4" >
      <!-- Adjust the height to your needs, mine is 40 -->
      <img :src="require('./assets/logo.png')" height="50"/>
      <v-spacer><h3 style="text-align: right;">Anmeldung Kinderlager</h3></v-spacer>
    </v-app-bar>

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

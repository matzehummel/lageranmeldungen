import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "495c41",
        secondary: 'ddd6c4',
        accent: 'b0af9a',
        error: 'cb8764',
        //warning: '$warning',
        //info: '$info',
      },
    },
  },
});
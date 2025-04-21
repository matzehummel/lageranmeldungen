<template>
  <v-container>
    <v-row>
      <v-col><h1 style="text-align: center; color: #495c41;">Willkommen bei der Anmeldung für's XXL-Lager {{currentYear}}!</h1></v-col>
    </v-row>
    <v-form ref="signupForm">
      <v-row>

  </v-row>
      <v-row class="text-center">
        <v-col md="8" xs="12" class="mx-auto my-2">
          <v-card v-if="validationStatus === 'failed'" prepend-icon="alert-circle" color="error" class="my-3 mx-auto">
            <v-card-text><v-icon class="mx-2">mdi-alert-circle</v-icon>Da stimmt wohl etwas noch nicht ganz!</v-card-text>
          </v-card>
          <v-card v-if="validationStatus === 'successful'" prepend-icon="alert-circle" color="primary" class="my-3 mx-auto">
            <v-card-text style="color: white;"><v-icon class="mx-2" style="color: white;">mdi-check-circle</v-icon>
              Das sieht doch schonmal super aus! Schau Dir nochmal alles an, ob das so passt.</v-card-text>
          </v-card>
          <p style="text-align: left;">Felder, die mit * gekennzeichnet sind, müssen ausgefüllt werden.</p>
          <v-row>
            <v-col cols="12" md="12" xs="12">
              <v-radio-group label="Geschlecht"
                  required v-model="sexe" :rules="nameRules">
                <v-radio label="Junge" value="m"></v-radio>
                <v-radio label="Mädchen" value="w"></v-radio>
              </v-radio-group>
            </v-col>
          </v-row>
          <v-row class="text-center">
            <v-col
              cols="12"
              md="6" xs="12"
            >
              <v-text-field
                v-model="childLastName"
                :rules="nameRules"
                label="Nachname des Kindes *"
                required
              ></v-text-field>
            </v-col>

            <v-col
                cols="12"
                md="6" xs="12"
              >
                <v-text-field
                  v-model="childFirstName"
                  :rules="nameRules"
                  label="Vorname des Kindes *"
                  required
                ></v-text-field>
            </v-col>

            <v-col
                cols="12"
                md="6" xs="12"
              >
                <v-text-field
                  v-model="parentsLastName"
                  :rules="nameRules"
                  label="Nachname der/des Erziehungsberechtigten *"
                  required
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="6" xs="12">
              <v-text-field
                  v-model="parentsFirstName"
                  :rules="nameRules"
                  label="Vorname der/des Erziehungsberechtigten *"
                  required
                  color="primary"
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="6" xs="12">
              <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                :return-value.sync="birthday"
                transition="scale-transition"
                offset-y
                min-width="290px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="birthday"
                    label="Geburtstag des/der Teilnehmenden *"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                    :rules="birthdayRules"
                  ></v-text-field>
                </template>
                <v-date-picker
                  ref="picker"
                  max="2010-12-31"
                  min="2007-01-01"
                  @change="save"
                ></v-date-picker>
                <!--<v-date-picker v-model="birthday" no-title scrollable locale="de" required>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                  <v-btn text color="primary" @click="$refs.menu.save(birthday)">OK</v-btn>
                </v-date-picker>-->
              </v-menu>
            </v-col>

            <v-col cols="12" md="6" xs="12">
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-Mail-Adresse *"
                required
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="6" xs="12">
              <v-text-field
                  v-model="phone"
                  label="Telefonnummer *"
                  :rules="nameRules"
                  required
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="6" xs="12">
              <v-text-field
                  v-model="phoneAlternative"
                  label="Alternative Telefonnummer"
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="5" xs="12">
              <v-text-field
                  v-model="address"
                  label="Straße und Hausnummer *"
                  :rules="nameRules"
                  required
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="2" xs="12">
              <v-text-field
                  v-model="plz"
                  label="PLZ *"
                  :rules="nameRules"
                  required
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="5" xs="12">
              <v-text-field
                  v-model="city"
                  label="Ort *"
                  :rules="nameRules"
                  required
                ></v-text-field>
            </v-col>

            <v-col cols="12" md="12" xs="12">
              <v-select
                  v-model="memberOf"
                  label="Ich bin Mitglied bei ... *"
                  :items="['Ministranten Bräunlingen', 'Ministranten Döggingen', 'Nirgends, aber ich hab\' trotzdem Lust auf\'s Zeltlager']"
                  required
                  :rules="selectRules"
                ></v-select>
            </v-col>

            <v-col cols="12" md="6" xs="12">
              <v-select
                  v-model="experienceKinderlager"
                  label="Auf dem Kinderlager war ich ... *"
                  :items="['nie dabei', '1 mal dabei', '2 mal dabei', '3 mal dabei', '4 mal dabei']"
                  required
                  :rules="selectRules"
                ></v-select>
            </v-col>
            <v-col cols="12" md="6" xs="12">
              <v-select
                  v-model="experienceXXL"
                  label="Auf dem XXL war ich ... *"
                  :items="['noch nie dabei', '1 mal dabei', '2 mal dabei']"
                  required
                  :rules="selectRules"
                ></v-select>
            </v-col>

            <v-col cols="12" md="4" xs="12">
              <v-text-field
                  v-model="insurance"
                  label="Ich bin krankenversichert bei ... *"
                  required
                  :rules="nameRules"
                ></v-text-field>
            </v-col>
            <v-col cols="12" md="5" xs="12">
              <v-text-field
                  v-model="doctor"
                  label="Mein Hausarzt ... *"
                  required
                  :rules="nameRules"
                ></v-text-field>
            </v-col>
            <v-col cols="12" md="3" xs="12">
              <v-radio-group label="Gegen Tetanus ..." required v-model="tetanus">
                <v-radio label="bin ich geimpft" value="1"></v-radio>
                <v-radio label="bin ich NICHT geimpft" value="0"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col cols="12" md="3" xs="12">
              <v-radio-group label="Ich kann ..." required v-model="swim">
                <v-radio label="schwimmen" value="1"></v-radio>
                <v-radio label="NICHT schwimmen" value="0"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col cols="12" md="9" xs="12">
              <v-radio-group label="Das Baden in öffentlichen Schwimmbädern unter Aufsicht der Leiter:innen wird mir ..." required v-model="swimAllowed">
                <v-radio label="erlaubt" value="1"></v-radio>
                <v-radio label="NICHT erlaubt" value="0"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col cols="12" md="3" xs="12">
              <v-radio-group label="Ich ernähre mich ..." required v-model="vegetarian">
                <v-radio label="NICHT vegetarisch" value="0"></v-radio>
                <v-radio label="vegetarisch" value="1"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col cols="12" md="9" xs="12">
              <v-radio-group label="Wir beziehen die Frischmilch zum Frühstück oft direkt vom Bauern vor Ort. Diese ist jedoch nicht immer abgekocht, weswegen die Keimfreiheit nicht gewährleistet ist. Ich darf ..."
                  required v-model="milk">
                <v-radio label="ungekochte, frische Milch trinken" value="1"></v-radio>
                <v-radio label="KEINE ungekochte, frische Milch trinken" value="0"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col cols="12" md="12" xs="12">
              <p style="text-align:left">Folgende besonderen Krankheiten, Allergien, Lebensmittelunverträglichkeiten, Operationen, Unfälle, etc. verlangen während des Zeltlagers in besonderer Weise Vorsicht und Rücksichtnahme (bitte auch Auflistung von Medikamenten, die während der Freizeit zu nehmen sind):</p>
              <v-textarea background-color="accent"
                  v-model="issues"
                ></v-textarea>
            </v-col>
            <v-col cols="12" md="9" xs="12">
              <v-radio-group label="Meine Erziehungsberechtigten sind während des Zeltlagers"
                  required v-model="availability">
                <v-radio label="unter obiger Anschrift zu erreichen" value="1"></v-radio>
                <v-radio label="im Urlaub unter folgender Anschrift zu erreichen:" value="2"></v-radio>
                <v-radio label="nicht zu erreichen, folgende Personen können als Kontaktpersonen angesprochen werden:" value="3"></v-radio>
              </v-radio-group>
            </v-col>
            <v-col cols="12" md="12" xs="12" v-if="availability !='1'">
              <v-textarea
                  v-model="alternativeAddress" background-color="accent" label="Alternative Erreichbarkeit"
                ></v-textarea>
            </v-col>
            <v-col cols="12" md="12" xs="12">
              <v-textarea
                  v-model="sonst" label="Das wäre mir noch ein Anliegen ..." background-color="accent"
                ></v-textarea>
            </v-col>
            <v-col cols="12" md="12" xs="12">
              <v-checkbox :label=checkboxTextAufsicht required :rules="checkboxRule"></v-checkbox>
            </v-col>
            <v-col cols="12" md="12" xs="12">
              <v-checkbox :label=checkboxTextBilder required :rules="checkboxRule"></v-checkbox>
            </v-col>
            <v-col cols="12" md="12" xs="12">
              <v-checkbox :label=checkboxTextErsteHilfe required :rules="checkboxRule"></v-checkbox>
            </v-col>
            <v-col cols="12" md="12" xs="12">
              <v-checkbox :label=checkboxTextPKW required :rules="checkboxRule"></v-checkbox>
            </v-col>
        </v-row>
        
      </v-col>
    </v-row>
  </v-form>

  <v-row>
    <v-col class="mx-auto" style="text-align: center;">
      <v-btn mb-4 x-large v-if="(validationStatus === 'none') || (validationStatus === 'failed')" color="primary" @click="validateForm(); scrollToTop()">
        Weiter
      </v-btn>
    </v-col>
  </v-row>
  <v-row class="my-5" v-if="validationStatus === 'successful'">
    <v-col md="8" sm="10" class="mx-auto">
      <h2 style=" color: #495c41;">Weiterer Ablauf</h2>
        <p style="text-align: left;">Nachdem Du Deine Brieftaube mit der Anmeldung zu uns losgeschickt hast, erhältst Du nochmal eine Bestätigungsmail.
          In dieser Bestätigungsmail sind Deine angegebenen Daten als PDF angehängt. Drucke das PDF aus, lass es von Deinen Eltern unterschreiben und
          <!-- bring das unterschriebene Formular zum Vortreffen mit. -->
          wirf das unterschriebene Formular in den Briefkasten des Pfarrbüros in Bräunlingen (Hüfingerstr. 2).
          <!-- Alternativ kannst Du es auch im Vorhinein bei einem Lagerleiter oder im Pfarrbüro einwerfen. -->
          Die Zusammenfassung und den Termin zum Vortreffen erhältst Du rechtzeitig per E-Mail.</p>
          <p style="text-align: left;">Nach dem Anmeldeschluss wird es eine erste Lagerpost geben,
          in der alles Weitere näher beschrieben wird. Diese werden wir per E-Mail an die oben genannte Adresse versenden. Das Vortreffen wird Anfang Juli stattfinden.
          Dort werden wir Euch alle noch offenen Fragen beantworten.</p>
        <p style="text-align: left;">Wir freuen uns auf ein superschönes Lager {{currentYear}} mit Euch!<br><br>Liebe Grüße, Euer Zeltlager-Team</p>
    </v-col>
  </v-row>
  <v-row v-if="loading">
    <v-col class="mx-auto" style="text-align: center;">
      <v-progress-circular
        indeterminate
        color="primary"
        size="64"
      ></v-progress-circular>
    </v-col>
  </v-row>
  <v-row>
    <v-col class="mx-auto" style="text-align: center;">
      <v-btn v-if="validationStatus === 'successful'" mb-4 x-large  color="primary" @click="confirmRegistration()" :disabled="confirmButtonDisabled">
        <v-icon class="mx-2">{{ confirmButtonIcon }}</v-icon> {{ confirmButtonText }}
        <!-- {{ confirmButtonText }} -->
      </v-btn>
    </v-col>
  </v-row>
    

  </v-container>
</template>

<script>
import axios from 'axios'
import * as config from "@/config";
import { ref } from 'vue';

  export default {
    name: 'HelloWorld',
    sendingDataSuccess: false,

    setup() {
      const currentYear = ref(config.currentYear);
      return { currentYear }
    },

    data () {
      return {
        form: true,
        validationStatus: "none",
        formHasErros: false,

        childLastName: '',
        childFirstName: '',
        parentsLastName: '',
        parentsFirstName: '',
        nameRules: [
          value => {
            if (value) return true
            return 'Bitte ausfüllen.'
          }
        ],

        menu: false,
        birthday: new Date().toISOString().substring(0,10),
        birthdayRules: [
          value => {
            if (new Date(value) > config.maxBirthday) return 'Du bist vielleicht noch etwas zu jung für\'s XXL. Wie wär\'s mit dem Kinderlager? :)'
            if (new Date(value) < config.minBirthday) return 'Du bist ja schon über 17! Magst du vielleicht als Leiter mitkommen? :)'
            return true 
          },
        ],
        email: '',
        emailRules: [
          value => {
            if (value) return true
            return 'Bitte eine E-Mail-Adresse angeben.'
          },
          value => {
            if (/.+@.+\..+/.test(value)) return true
            return 'Diese E-Mail-Adresse ist nicht gültig.'
          },
        ],

        phone: '',
        phoneAlternative: '',
        address: '',
        plz: '',
        city: '',

        memberOf: '',
        experienceKinderlager: '',
        experienceXXL: '',
        selectRules: [
          value => {
            if (value) return true
            return 'Bitte auswählen.'
          },
        ],
        
        insurance: "",
        doctor: "",
        tetanus: "1",
        swim: "1",
        swimAllowed: "1",
        vegetarian: "0",
        milk: "1",
        issues: "",
        availability: "1",
        alternativeAddress: "",
        sonst: "",

        checkboxTextAufsicht: "Für die Dauer der Freizeit wird das Erziehungsrecht und die Aufsichtspflicht den Leiter*innen übertragen. *",
        checkboxTextBilder: "Meine Erziehungsberechtigten erlauben dem Zeltlager, Bilder auf denen ich zu sehen bin, in einem Diavortrag bzw. in der Zeitung oder auf der Webseite zu veröffentlichen. *",
        checkboxTextErsteHilfe: "Meine Erziehungsberechtigten erlauben, dass mir in Notfällen Erste Hilfe geleistet werden darf. Insektenstiche, kleine Wunden und leichte gesundheitliche Beschwerden dürfen versorgt und Zecken entfernt werden. Bei schwereren (oder schlimmeren) Verletzungen und schweren gesundheitlichen Beschwerden wird ein Arzt oder Krankenhaus aufgesucht. *",
        checkboxTextPKW: "Meine Erziehungsberechtigten erlauben, dass ich ggf. (z.B. Weg zum Arzt) in einem Privat-PKW bei einem/einer Leiter*in mitfahren darf. *",
        checkboxRule: [
          value => {
            if(value) return true
            return 'Für die Anmeldung ist eine Zustimmung erforderlich.'
          }
        ],

        loading: false,
        confirmButtonDisabled: false,
        confirmButtonText: "Anmeldung bestätigen!",
        confirmButtonIcon: "mdi-thumb-up"
      }
    },

    watch: {
      menu (val) {
        val && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
      },
    },
    methods: {
      save (birthday) {
        this.$refs.menu.save(birthday)
      },
      async validateForm() {
        const result = await this.$refs.signupForm.validate()
        console.log(result);
        if(result) {
          this.form = false
          this.validationStatus = "successful"
        } else {
          this.validationStatus = "failed"
        }
        return result;
      },
      scrollToTop() {
        window.scrollTo(0,0);
      },
      async confirmRegistration() {
        this.loading = true;
        this.confirmButtonIcon = "mdi-check-circle"
        this.confirmButtonText = "Anmeldung wird übermittelt ..."
        const valid = await this.validateForm();
        if(valid) {
          this.confirmButtonDisabled = true;
          await this.sendData();
          if(this.sendingDataSuccess) {
            console.log("Data sent successfully");
            window.location.assign('https://zeltlager-braeunlingen.de/du-bist-angemeldet/');
          } else {
            console.log("Error sending data");
            // TODO: Go to Error Page
          }
        } else {
          this.confirmButtonDisabled = false;
          this.scrollToTop()
        }
      },
      async sendData() {
        
        const endpoint = "/registration/xxl";
        var payload = {
          sexe: this.sexe,
          childLastName: this.childLastName,
          childFirstName: this.childFirstName,
          parentsLastName: this.parentsLastName,
          parentsFirstName: this.parentsFirstName, 
          birthday: this.birthday,
          email: this.email,
          phone: this.phone,
          phoneAlternative: this.phoneAlternative,
          address: this.address,
          plz: this.plz,
          city: this.city,
          memberOf: this.memberOf,
          experienceKinderlager: this.experienceKinderlager,
          experienceXXL: this.experienceXXL,
          supervisors: this.supervisors,
          insurance: this.insurance,
          doctor: this.doctor,
          tetanus: this.tetanus,
          swim: this.swim,
          swimAllowed: this.swimAllowed,
          vegetarian: this.vegetarian,
          milk: this.milk,
          issues: this.issues,
          availability: this.availability,
          alternativeAddress: this.alternativeAddress,
          sonst: this.sonst,
        };
        await axios.post('https://backend.zeltlager-braeunlingen.de' + endpoint,
        // await axios.post('http://localhost:5000' + endpoint, )
          payload
        )
        .then(response => {
          console.log(response.data)
          if(response.status === 200) {
            this.sendingDataSuccess = true;
          } else {
            this.sendingDataSuccess = false;
          }
        })
        .catch(error => {
          console.log(error)
          this.sendingDataSuccess = false;
        })

      }
    }
  }
</script>

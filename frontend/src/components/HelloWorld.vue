<template>
  <v-container >
    <v-row class="text-center">
      <v-col md="8" xs="12" class="mx-auto my-2">
        <!--<v-row>
          <h2>Persönliche Angaben</h2>
        </v-row>-->

        <v-row class="text-center">
          <v-col
              cols="12"
              md="6" xs="12"
            >
              <v-text-field
                v-model="firstname"
                :rules="nameRules"
                label="Nachname des Kindes"
                required
              ></v-text-field>
          </v-col>

          <v-col
              cols="12"
              md="6" xs="12"
            >
              <v-text-field
                v-model="secondname"
                :rules="nameRules"
                label="Vorname des Kindes"
                required
              ></v-text-field>
          </v-col>

          <v-col
              cols="12"
              md="6" xs="12"
            >
              <v-text-field
                v-model="firstname"
                :rules="nameRules"
                label="Nachname der/des Erziehungsberechtigten"
                required
              ></v-text-field>
          </v-col>

          <v-col cols="12" md="6" xs="12">
            <v-text-field
                v-model="secondname"
                :rules="nameRules"
                label="Vorname der/des Erziehungsberechtigten"
                required
              ></v-text-field>
          </v-col>

          <v-col cols="12" md="6" xs="12">
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              :return-value.sync="date"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="date"
                  label="Geburtstag des Kindes"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="date" no-title scrollable locale="de" required>
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
              </v-date-picker>
            </v-menu>
          </v-col>

          <v-col cols="12" md="6" xs="12">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-Mail"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6" xs="12">
            <v-text-field
                v-model="secondname"
                label="Telefonnummer"
                required
              ></v-text-field>
          </v-col>

          <v-col cols="12" md="6" xs="12">
            <v-text-field
                v-model="secondname"
                label="Straße und Hausnummer"
                required
              ></v-text-field>
          </v-col>

          <v-col cols="12" md="4" xs="12">
            <v-text-field
                v-model="secondname"
                label="PLZ"
                required
              ></v-text-field>
          </v-col>

          <v-col cols="12" md="8" xs="12">
            <v-text-field
                v-model="secondname"
                label="Ort"
                required
              ></v-text-field>
          </v-col>

          <v-col cols="12" md="6" xs="12">
            <v-select
                v-model="secondname"
                label="Ich bin Mitglied bei ..."
                :items="['Ministranten Bräunlingen', 'Ministranten Döggingen', 'Nirgends, aber ich hab\' trotzdem Lust auf\'s Zeltlager']"
                required
              ></v-select>
          </v-col>

          <v-col cols="12" md="6" xs="12">
            <v-select
                v-model="secondname"
                label="Ich war ..."
                :items="['schon einmal auf dem Zeltlager dabei', 'noch nie dabei']"
                required
              ></v-select>
          </v-col>

          <v-col cols="12" md="12" xs="12">
            <v-text-field
                v-model="secondname"
                label="Meine Gruppenleiter:innen sind ..."
                required
              ></v-text-field>
          </v-col>
          
        </v-row>
        <!--<v-row>
          <h2>Gesundheitsfragen</h2>
        </v-row>-->
        <v-row>
          <v-col cols="12" md="6" xs="12">
            <v-text-field
                v-model="secondname"
                label="Ich bin krankenversichert bei ..."
                required
              ></v-text-field>
          </v-col>
          <v-col cols="12" md="6" xs="12">
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
            <p style="text-align:left">Folgende besonderen Krankheiten, Allergien, Lebensmittelverträglichkeiten, Operationen, Unfälle, etc. verlangen während dem Zeltlager in besonderer Weise Vorsicht und Rücksichtnahme (bitte auch Auflistung von Medikamenten, die während der Freizeit zu nehmen sind):</p>
            <v-textarea
                v-model="secondname"
              ></v-textarea>
          </v-col>
          <v-col cols="12" md="9" xs="12">
            <v-radio-group label="Meine Erziehungsberechtigten sind während dem Zeltlager"
                required v-model="availability">
              <v-radio label="unter obiger Anschrift zu erreichen" value="1"></v-radio>
              <v-radio label="im Urlaub unter folgender Anschrift zu erreichen:" value="2"></v-radio>
              <v-radio label="nicht zu erreichen, folgende Personen können als Kontaktpersonen angesprochen werden:" value="3"></v-radio>
            </v-radio-group>
          </v-col>
          <v-col cols="12" md="12" xs="12" v-if="availability !='1'">
            <v-textarea
                v-model="secondname" background-color="secondary"
              ></v-textarea>
          </v-col>
          <v-col cols="12" md="12" xs="12">
            <v-textarea
                v-model="secondname" label="Das wäre mir noch ein Anliegen ..."
              ></v-textarea>
          </v-col>
          <v-col cols="12" md="12" xs="12">
            <v-checkbox :label=checkboxTextAufsicht required></v-checkbox>
          </v-col>
          <v-col cols="12" md="12" xs="12">
            <v-checkbox :label=checkboxTextBilder required></v-checkbox>
          </v-col>
          <v-col cols="12" md="12" xs="12">
            <v-checkbox :label=checkboxTextErsteHilfe required></v-checkbox>
          </v-col>
          <v-col cols="12" md="12" xs="12">
            <v-checkbox :label=checkboxTextPKW required></v-checkbox>
          </v-col>
          <v-row class="my-5">
            <h2>Weiterer Ablauf</h2>
            <p style="text-align: left;">Nachdem Du Deine Brieftaube mit der Anmeldung zu uns losgeschickt habt, erhältst Du nochmal eine Bestätigungsmail mit den angegebenen Daten.
              Vor dem Vortreffen erhältst Du die hier angegebenen Daten zur Bestätigung nochmal zugestellt.
              Die Zusammenfassung Deiner Daten lässt Du von Deinen Eltern unterschreiben und bringst sie zum Vortreffen mit.
              Alternativ kannst Du es auch im Vorhinein bei einem Lagerleiter oder im Pfarrbüro einwerfen.
              Die Zusammenfassung und den Termin zum Vortreffen erhältst Du rechtzeitig per E-Mail.</p>
            <p style="text-align: left;">Nach dem Anmeldeschluss wird es eine erste Lagerpost geben,
              auf der alles Weitere näher beschrieben sein wird. Diese werden wir per E-Mail an die oben genannte Adresse versenden. Das Vortreffen wird Anfang Juli stattfinden.
              Dort werden wir Euch alle noch offenen Fragen beantworten.</p>
            <p style="text-align: left;">Wir freuen uns auf ein superschönes Lager 2023 mit Euch!<br></p>
            <p style="text-align: left;">Liebe Grüße, Euer Zeltlager-Team</p>
          </v-row>
        </v-row>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data () {
      return {
        date: new Date().toISOString().substring(0,10),
        menu: false,
        tetanus: "1",
        swim: "1",
        swimAllowed: "1",
        vegetarian: "0",
        milk: "1",
        availability: "1",

        checkboxTextAufsicht: "Für die Dauer der Freizeit wird das Erziehungsrecht und die Aufsichtspflicht den Leiter*innen übertragen.",
        checkboxTextBilder: "Meine Erziehungsberechtigten erlauben dem Zeltlager Bilder auf denen ich zu sehen bin, in einem Diavortrag bzw. in der Zeitung oder auf der Webseite zu veröffentlichen. ",
        checkboxTextErsteHilfe: "Meine Erziehungsberechtigten erlauben, dass mir in Notfällen Erste Hilfe geleistet werden darf. Insektenstiche, kleine Wunden und leichte gesundheitliche Beschwerden dürfen versorgt und Zecken mithilfe einer Zeckenzange entfernt werden. Bei schwereren (oder schlimmeren) Verletzungen und schweren gesundheitlichen Beschwerden wird ein Arzt oder Krankenhaus aufgesucht. ",
        checkboxTextPKW: "Meine Erziehungsberechtigten erlauben, dass ich in einem Privat-PKW bei einem/einer Leiter*in mitfahren darf."
      }
    },
  }
</script>

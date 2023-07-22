import { createApp } from 'vue'
import router from './router/index.js'
//import './style.css'
import App from './App.vue'
import piniaPluginPersistedState from "pinia-plugin-persistedstate"

import { createPinia } from 'pinia'
const pinia = createPinia()
pinia.use(piniaPluginPersistedState)

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
const app = createApp(App)
library.add(fas, fab)
app.use(pinia)

app.use()
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')

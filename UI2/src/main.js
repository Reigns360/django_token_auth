import '@/@iconify/icons-bundle'
import App from '@/App.vue'
import vuetify from '@/plugins/vuetify'
import { loadFonts } from '@/plugins/webfontloader'
import router from '@/router'
import '@core/scss/template/index.scss'
import '@layouts/styles/index.scss'
import '@styles/styles.scss'
import 'bootstrap/dist/css/bootstrap.css'
import { createPinia } from 'pinia'
import Swal from 'sweetalert2'
import { createApp } from 'vue'
import store from './store'

// Import your Vuex store
//Base Url
window.$http = 'http://localhost:8000/api/'
console.log

loadFonts()


// Create vue app
const app = createApp(App)

app.config.globalProperties.$swal = Swal

// Use plugins
app.use(vuetify)
app.use(createPinia())
app.use(router)
app.use(store)

// Mount vue app
app.mount('#app')

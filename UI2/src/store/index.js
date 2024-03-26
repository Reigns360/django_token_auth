import { createStore } from 'vuex'
import authModule from './modules/auth' // Import your 'auth' module

const store = createStore({
  modules: {
    auth: authModule,
  },
})

export default store

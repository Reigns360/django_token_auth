import { createStore } from 'vuex'
import authModule from './modules/auth' // Import your 'auth' module
import setupModule from './modules/setup'

const store = createStore({
  modules: {
    auth: authModule,
    setup: setupModule,
  },
})

export default store
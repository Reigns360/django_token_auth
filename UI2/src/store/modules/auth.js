import axios from '@/axiosConfig'

const state = {
  isAuthenticated: false,
  user: null,
}

const mutations = {
  SET_AUTHENTICATED(state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated
  },
  SET_USER(state, user) {
    state.user = user
  },
}

const actions = {
  async login({ commit }, payload) {
    try {
      const response = await axios.post('login/', payload)

      console.log(response)// x,y=1,2

      const { token, user } = response.data

      if (user.role === "Admin") {
        sessionStorage.setItem('isAdmin', true)
      } else {
        sessionStorage.setItem('isAdmin', false)
      }
      commit('SET_AUTHENTICATED', true)
      sessionStorage.setItem('token', token)
      sessionStorage.setItem('user', user)
      commit('SET_USER', user)
    } catch (error) {
      // Modify this part to include the response message in the error
      let errorMessage = 'An error occurred during login.'
      if (error.response && error.response.data && error.response.data.error) {
        errorMessage = error.response.data.error
      }
      throw new Error(errorMessage)
    }
  },

  logout({ commit }) {
    sessionStorage.removeItem('token')
    sessionStorage.removeItem('user')
    sessionStorage.removeItem('isAdmin')
    commit('SET_AUTHENTICATED', false, false)
    commit('SET_USER', null)
  },

  checkAuthentication({ commit }) {
    const token = sessionStorage.getItem('token')
    const user = this.sessionStorage.getItem('user')
    if (token) {
      commit('SET_AUTHENTICATED', true)
      commit('SET_USER', user)
    }
  },
}

export default {
  namespaced: true, 
  state,
  mutations,
  actions,
}

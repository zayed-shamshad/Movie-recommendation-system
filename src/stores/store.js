//user store in pinia

import { defineStore } from 'pinia'
export const useUserStore = defineStore({
    id: 'user',
    //user store
    state: () => ({
        user: null,
    }),
    getters: {
        getUser: (state) => {
            console.log("fetching user value",state.user);
            return state.user
        }
    },
    actions: {
        setUser(userdata) {
           this.user=userdata;
           console.log("user value set to ",this.user)
        },
    },
    persist: true,
})

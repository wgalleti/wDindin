import state from "@/store/state.js";
import authStore from "@/store/auth";
import { defineStore } from "pinia";

export const useStore = defineStore("core", {
  state: () => state,
  actions: {
    setStores() {
      this.auth = authStore();
    },
  },
});

export default useStore;

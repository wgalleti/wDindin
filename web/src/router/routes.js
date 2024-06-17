import HomeView from "@/pages/index";
import LoginView from "@/pages/login";

export const routes = [
  { path: "/", component: HomeView },
  {
    path: "/login",
    component: LoginView,
    meta: {
      requiresAuth: false,
    },
  },
];

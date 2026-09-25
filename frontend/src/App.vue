<template>
  <router-view />
</template>

<script setup>
import { createRouter, createWebHistory } from 'vue-router';
import RegulationList from './components/RegulationList.vue';
import RegulationDetail from './components/RegulationDetail.vue';
import UserLogin from './components/UserLogin.vue';

const routes = [
  { path: '/', name: 'RegulationList', component: RegulationList },
  { path: '/regulation/:id', name: 'RegulationDetail', component: RegulationDetail, props: true },
  { path: '/login', name: 'Login', component: UserLogin },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
</script>

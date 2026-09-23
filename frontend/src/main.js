import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';

axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000/api';

const app = createApp(App);
app.config.globalProperties.$axios = axios;
app.mount('#app');

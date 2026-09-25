<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username</label>
        <input id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input id="password" type="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const router = useRouter();

const login = async () => {
  try {
    const res = await axios.post('/api/auth/login', {
      username: username.value,
      password: password.value,
    });
    localStorage.setItem('token', res.data.access_token);
    router.push({ name: 'RegulationList' });
  } catch (err) {
    console.error(err);
    alert('Login failed');
  }
};
</script>

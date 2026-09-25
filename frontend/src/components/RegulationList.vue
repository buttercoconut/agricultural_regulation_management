<template>
  <div>
    <h2>Regulation List</h2>
    <div>
      <input v-model="search" placeholder="Search by title" @input="fetchRegulations(1)" />
    </div>
    <ul>
      <li v-for="reg in regulations" :key="reg.id">
        <router-link :to="{ name: 'RegulationDetail', params: { id: reg.id } }">
          {{ reg.title }} ({{ reg.status }})
        </router-link>
      </li>
    </ul>
    <div>
      <button @click="prevPage" :disabled="page <= 1">Prev</button>
      <span>Page {{ page }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="page >= totalPages">Next</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const regulations = ref([]);
const page = ref(1);
const pageSize = 10;
const totalPages = ref(1);
const search = ref('');

const fetchRegulations = async (p = 1) => {
  try {
    const res = await axios.get('/api/regulations', {
      params: { page: p, page_size: pageSize, search: search.value },
    });
    regulations.value = res.data.items;
    totalPages.value = Math.ceil(res.data.total / pageSize);
    page.value = p;
  } catch (err) {
    console.error(err);
  }
};

const nextPage = () => {
  if (page.value < totalPages.value) fetchRegulations(page.value + 1);
};
const prevPage = () => {
  if (page.value > 1) fetchRegulations(page.value - 1);
};

onMounted(() => fetchRegulations());
</script>

<style scoped>
ul { list-style: none; padding: 0; }
li { margin: 5px 0; }
</style>

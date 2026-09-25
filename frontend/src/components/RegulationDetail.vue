<template>
  <div>
    <h2>Regulation Detail</h2>
    <div v-if="regulation">
      <p><strong>ID:</strong> {{ regulation.id }}</p>
      <p><strong>Title:</strong> {{ regulation.title }}</p>
      <p><strong>Description:</strong> {{ regulation.description }}</p>
      <p><strong>Status:</strong> {{ regulation.status }}</p>
      <p><strong>Effective Date:</strong> {{ regulation.effective_date }}</p>
      <p><strong>Regions:</strong> {{ regulation.region_ids.join(', ') }}</p>
      <p><strong>Categories:</strong> {{ regulation.category_ids.join(', ') }}</p>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const regulation = ref(null);

const fetchRegulation = async () => {
  try {
    const res = await axios.get(`/api/regulations/${route.params.id}`);
    regulation.value = res.data;
  } catch (err) {
    console.error(err);
  }
};

onMounted(() => {
  fetchRegulation();
});
</script>

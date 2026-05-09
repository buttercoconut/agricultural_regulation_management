<template>
  <div class="regulation-list">
    <h1>농업 규제 목록</h1>
    <ul>
      <li v-for="reg in regulations" :key="reg.id">
        <router-link :to="{ name: 'RegulationDetail', params: { id: reg.id } }">
          {{ reg.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const regulations = ref([])

onMounted(async () => {
  // Mock API call – replace with real backend endpoint
  const response = await fetch('https://api.example.com/regulations')
  if (response.ok) {
    regulations.value = await response.json()
  } else {
    // Fallback data
    regulations.value = [
      { id: 1, title: '농업법 개정안' },
      { id: 2, title: '농산물 수출 규제' },
    ]
  }
})
</script>

<style scoped>
.regulation-list {
  padding: 1rem;
}
</style>

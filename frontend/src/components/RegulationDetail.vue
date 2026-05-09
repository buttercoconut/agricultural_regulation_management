<template>
  <div class="regulation-detail">
    <h1>{{ regulation.title }}</h1>
    <p>{{ regulation.content }}</p>
    <router-link :to="{ name: 'Home' }">목록으로 돌아가기</router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const regulation = ref({ title: '', content: '' })

onMounted(async () => {
  const id = route.params.id
  // Mock API call – replace with real backend endpoint
  const response = await fetch(`https://api.example.com/regulations/${id}`)
  if (response.ok) {
    regulation.value = await response.json()
  } else {
    regulation.value = {
      title: '예시 규제 제목',
      content: '예시 규제 내용입니다. 실제 API에서 가져온 데이터를 표시합니다.',
    }
  }
})
</script>

<style scoped>
.regulation-detail {
  padding: 1rem;
}
</style>

<template>
  <div class="regulation-list">
    <h2>규제 목록</h2>
    <input v-model="search" placeholder="검색어 입력" @input="fetchRegulations" />
    <table>
      <thead>
        <tr>
          <th>제목</th>
          <th>유형</th>
          <th>지역</th>
          <th>등록일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="reg in regulations" :key="reg.id">
          <td>{{ reg.title }}</td>
          <td>{{ reg.category }}</td>
          <td>{{ reg.region }}</td>
          <td>{{ formatDate(reg.created_at) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'RegulationList',
  data() {
    return {
      regulations: [],
      search: '',
    };
  },
  methods: {
    async fetchRegulations() {
      try {
        const response = await this.$axios.get('/regulations', {
          params: { q: this.search },
        });
        this.regulations = response.data;
      } catch (err) {
        console.error('Error fetching regulations:', err);
      }
    },
    formatDate(dateStr) {
      const d = new Date(dateStr);
      return d.toLocaleDateString();
    },
  },
  mounted() {
    this.fetchRegulations();
  },
};
</script>

<style scoped>
.regulation-list {
  max-width: 800px;
  margin: auto;
}
input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}
th {
  background-color: #f2f2f2;
}
</style>

<template>
  <div id="app">
    <h1>농업 규제 관리 시스템</h1>
    <RegulationList />
  </div>
</template>

<script>
import RegulationList from './components/RegulationList.vue';
export default {
  name: 'App',
  components: { RegulationList },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 20px;
}
</style>

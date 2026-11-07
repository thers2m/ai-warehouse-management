<script setup>
import { ref, onMounted } from 'vue'
import { getInventory } from '../api/inventory'
import SectionHeader from '../components/SectionHeader.vue'
const rows = ref([]), loading = ref(false), error = ref('')
onMounted(async () => { loading.value = true; try { rows.value = (await getInventory()).data.data } catch (e) { error.value = e.message } finally { loading.value = false } })
</script>
<template>
  <SectionHeader title="Tồn kho" subtitle="Số lượng tồn theo sản phẩm" />
  <el-alert v-if="error" :title="error" type="error" show-icon style="margin-bottom:15px" />
  <el-card><el-table :data="rows" v-loading="loading" stripe><el-table-column prop="product_id" label="ID" width="90"/><el-table-column prop="name" label="Sản phẩm"/><el-table-column prop="stock_quantity" label="Số lượng tồn"/></el-table></el-card>
</template>

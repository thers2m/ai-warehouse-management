<script setup>
import { ref, onMounted } from 'vue'
import { getProducts } from '../api/products'
import SectionHeader from '../components/SectionHeader.vue'
const rows = ref([]), loading = ref(false), error = ref('')
onMounted(async () => { loading.value = true; try { rows.value = (await getProducts()).data.data } catch (e) { error.value = e.message } finally { loading.value = false } })
</script>
<template>
  <SectionHeader title="Sản phẩm" subtitle="Danh mục sản phẩm hiện có" />
  <el-alert v-if="error" :title="error" type="error" show-icon style="margin-bottom:15px" />
  <el-card><el-table :data="rows" v-loading="loading" stripe><el-table-column prop="id" label="ID" width="80"/><el-table-column prop="name" label="Tên sản phẩm"/><el-table-column prop="price" label="Giá"/><el-table-column prop="stock_quantity" label="Tồn kho"/><el-table-column prop="status" label="Trạng thái"/></el-table></el-card>
</template>

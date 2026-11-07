<script setup>
import { ref, onMounted } from 'vue'
import { getOrders } from '../api/orders'
import SectionHeader from '../components/SectionHeader.vue'
const rows = ref([]), loading = ref(false), error = ref('')
onMounted(async () => { loading.value = true; try { rows.value = (await getOrders()).data.data } catch (e) { error.value = e.message } finally { loading.value = false } })
</script>
<template>
  <SectionHeader title="Đơn hàng" subtitle="Danh sách đơn hàng, trạng thái duyệt" />
  <el-alert v-if="error" :title="error" type="error" show-icon style="margin-bottom:15px" />
  <el-card><el-table :data="rows" v-loading="loading" stripe><el-table-column prop="id" label="Mã đơn" width="90"/><el-table-column prop="customer_name" label="Khách hàng"/><el-table-column prop="total_amount" label="Tổng tiền"/><el-table-column prop="status" label="Trạng thái"/><el-table-column prop="created_at" label="Ngày tạo"/></el-table></el-card>
</template>

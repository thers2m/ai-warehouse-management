<script setup>
defineProps({ title: { type: String, required: true }, subtitle: String })
</script>
<template><header style="margin-bottom:20px"><h1 style="margin:0 0 4px">{{ title }}</h1><div style="color:#64748b">{{ subtitle }}</div></header></template>

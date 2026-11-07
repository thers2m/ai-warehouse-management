<template>
  <div style="display:flex; min-height:100vh">
    <aside class="sidebar">
      <div class="logo">📦 Warehouse AI</div>
      <RouterLink to="/" class="nav-link">Dashboard</RouterLink>
      <RouterLink to="/products" class="nav-link">Sản phẩm</RouterLink>
      <RouterLink to="/orders" class="nav-link">Đơn hàng</RouterLink>
      <RouterLink to="/inventory" class="nav-link">Tồn kho</RouterLink>
      <RouterLink to="/agent" class="nav-link">AI Assistant</RouterLink>
    </aside>
    <main class="content"><RouterView /></main>
  </div>
</template>

import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import ProductsView from '../views/ProductsView.vue'
import OrdersView from '../views/OrdersView.vue'
import InventoryView from '../views/InventoryView.vue'
import AgentChatView from '../views/AgentChatView.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: DashboardView },
    { path: '/products', component: ProductsView },
    { path: '/orders', component: OrdersView },
    { path: '/inventory', component: InventoryView },
    { path: '/agent', component: AgentChatView }
  ]
})

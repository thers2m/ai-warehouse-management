import { api } from './client'
export const getOrders = (status) => api.get('/orders', { params: status ? { status } : {} })

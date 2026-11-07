import { api } from './client'
export const getInventory = () => api.get('/inventory')

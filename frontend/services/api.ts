import axios from 'axios';

const api = axios.create({
  baseURL: 'https://your-render-backend-url', // Replace with Render URL
});

export const getRequests = (filters = {}) => api.get('/requests', { params: filters });
export const createRequest = (data: any) => api.post('/requests', data);
export const completeRequest = (id: number, fulfillerId: number) =>
  api.patch(`/requests/${id}/complete`, { fulfiller_id: fulfillerId });
export const getLeaderboard = (sortBy = 'xp') =>
  api.get('/users/leaderboard', { params: { sort: sortBy } });

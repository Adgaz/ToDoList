import axios from 'axios';
import type { TodoItem } from '../types/Todo';  // Add 'type' keyword

const API_BASE_URL = '/api/todo';

export const todoService = {
    async getAll(): Promise<TodoItem[]> {
        const response = await axios.get(API_BASE_URL);
        return response.data;
    },

    async getById(id: number): Promise<TodoItem> {
        const response = await axios.get(`${API_BASE_URL}/${id}`);
        return response.data;
    },

    async create(todo: Omit<TodoItem, 'id'>): Promise<TodoItem> {
        const response = await axios.post(API_BASE_URL, todo);
        return response.data;
    },

    async update(id: number, todo: TodoItem): Promise<void> {
        await axios.put(`${API_BASE_URL}/${id}`, todo);
    },

    async delete(id: number): Promise<void> {
        await axios.delete(`${API_BASE_URL}/${id}`);
    }
};

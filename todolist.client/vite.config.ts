import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
    plugins: [react()],
    server: {
        port: 54420,
        https: false,
        proxy: {
            '/api': {
                target: 'https://localhost:7217',
                changeOrigin: true,
                secure: false
            }
        }
    }
})

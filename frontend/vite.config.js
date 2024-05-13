import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';



export default defineConfig({
  server:{
    origin: 'demo.hah4.me',
  },
  plugins: [
    react()
  ]
});

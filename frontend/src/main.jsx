import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import { makeServer } from "../mock/server.js";
import './index.css';

if (process.env.NODE_ENV === 'development' &&
  typeof makeServer === 'function'
) {
  makeServer();
}


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);

import React from 'react';
import ReactDOM from 'react-dom/client';
import { makeServer } from "../mock/server.js";
import DefaultLayout from "./components/Layout/DefaultLayout/DefaultLayout.jsx";
import {Fragment} from "react";
import {publicRoutes} from "./routes";
import './index.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


if (import.meta.env.MODE === 'development' && typeof makeServer === 'function') {
  makeServer();
}



ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
    <Routes>
        {publicRoutes.map((route,index) =>{
          let Layout = DefaultLayout
          if(route.layout){
            Layout = route.layout
          }else if(route.layout === null){
            Layout = Fragment
          }
          const Page = route.component;
          return (<Route key={index} path ={route.path} element = {<Layout><Page/></Layout>}/>)
        })}
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
);

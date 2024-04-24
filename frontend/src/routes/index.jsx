import Login from '../pages/login';
import Homepage from '../pages/homepage';
import LoginLayout from '../components/Layout/LoginLayout';
import Patients from '../pages/patients';

const publicRoutes = [
    {
        path: '/',
        component: Homepage,
    },
    {
        path: '/login',
        component: Login,
        layout: LoginLayout
    },
    {
        path: '/patient',
        component: Patients,
    },
]

const privateRoutes = [
    
]


export {publicRoutes, privateRoutes}
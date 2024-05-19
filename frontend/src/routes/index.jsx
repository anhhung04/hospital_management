import Login from '../pages/login';
import Homepage from '../pages/homepage';
import LoginLayout from '../components/Layout/LoginLayout';
import Patients from '../pages/patients';
import Employee from '../pages/employee';

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
    {
        path: '/employee',
        component: Employee,
    },
]

const privateRoutes = [
    
]


export {publicRoutes, privateRoutes}
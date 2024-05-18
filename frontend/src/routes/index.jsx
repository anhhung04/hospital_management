import Login from '../pages/login';
import Homepage from '../pages/homepage';
import LoginLayout from '../components/Layout/LoginLayout';
import Patients from '../pages/patients';
import Medicines from '../pages/medicines';

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
        path: '/medicine',
        component: Medicines,
    }
]

const privateRoutes = [
    
]


export {publicRoutes, privateRoutes}
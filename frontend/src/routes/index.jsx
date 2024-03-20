import Login from '../pages/login';
import Homepage from '../pages/homepage';
import LoginLayout from '../components/Layout/LoginLayout';

const publicRoutes = [
    {
        path: '/',
        component: Homepage,
    },
    {
        path: '/login',
        component: Login,
        layout: LoginLayout
    }
]

const privateRoutes = [
    
]


export {publicRoutes, privateRoutes}
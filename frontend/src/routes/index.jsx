import Login from '../pages/login';
import Homepage from '../pages/homepage';
import LoginLayout from '../components/Layout/LoginLayout';
// import Employee from '../pages/employee';
// import Medicine from '../pages/medicine';
// import Equipment from '../pages/equipments';
// import Patients from '../pages/patients';

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
    // {
    //     path: '/patient',
    //     component: Patients,
    // },
    // {
    //     path: '/employee',
    //     component: Employee,
    // },
    // {
    //     path: '/medicine',
    //     component: Medicine,
    // },
    // {
    //     path: '/equipment',
    //     component: Equipment,
    // },
    
]

const privateRoutes = [
    
]


export {publicRoutes, privateRoutes}
import Header from "../DefaultLayout/Header";
import Footer from "../DefaultLayout/Footer";


function LoginLayout({children}) {

    return (
        <div className="flex flex-col h-full justify-between">
            <Header className="my-0 py-0"/>
            {children}
            <Footer/>
        </div>
    );
}

export default LoginLayout;

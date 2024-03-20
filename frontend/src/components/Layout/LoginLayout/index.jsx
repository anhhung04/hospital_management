import Header from "../DefaultLayout/Header";
import Footer from "../DefaultLayout/Footer";

function LoginLayout({children}) {
    return (
        <div class="flex flex-col h-screen justify-between">
            <Header class="my-0 py-0"/>
            {children}
            <Footer/>
        </div>
    );
}

export default LoginLayout;

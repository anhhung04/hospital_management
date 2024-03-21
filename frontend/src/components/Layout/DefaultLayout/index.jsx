import Header from "./Header";
import Footer from "./Footer";

function DefaultLayout({children}) {
    return (<div class="flex flex-col h-screen justify-between">
        <Header/>
        <div class="flex flex-row">
            <div class="flex-1 p-10">
                {children}
            </div>
        </div>
        <Footer/>
    </div> );
}

export default DefaultLayout;
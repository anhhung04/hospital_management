import Header from "./Header";
import Footer from "./Footer";

function DefaultLayout() {
    return (<div class="flex flex-col h-screen justify-between">
        <Header/>
        <div class="mb-auto">Content</div>
        <Footer/>
    </div> );
}

export default DefaultLayout;
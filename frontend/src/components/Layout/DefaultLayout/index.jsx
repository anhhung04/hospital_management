import Header from "./Header";
import Footer from "./Footer";

function DefaultLayout({children}) {
    const [current_content, setCurrent_content] = useState("general");  
    function handleClick(content) {
        setCurrent_content(content);
    }
    return (<div className="flex flex-col h-full w-full justify-between mb-0">
        <Header/>
        <div class="flex flex-row">
            <div class="flex-1 p-10">
                {children}
        </div>
        <Footer/>
    </div> );
}

export default DefaultLayout;


import Header from "./Header";
import Footer from "./Footer";

function DefaultLayout({children}) {
    // const [current_content, setCurrent_content] = useState("general");  
    // function handleClick(content) {
    //     setCurrent_content(content);
    // }
    return (<div className="flex flex-col h-full w-full justify-between mb-0">
        <Header/>
        <div className="flex flex-row">
            <div className="flex-1 p-10">
                {children}
            </div>
        </div>
        <Footer/>
    </div> );
}

export default DefaultLayout;


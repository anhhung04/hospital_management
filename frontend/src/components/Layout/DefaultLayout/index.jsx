import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./SideBar";
import { useState } from "react";


function DefaultLayout({children}) {
    const [current_content, setCurrent_content] = useState("general");  
    function handleClick(content) {
        setCurrent_content(content);
    }
    return (<div className="flex flex-col h-full w-full justify-between mb-0">
        <Header/>
        <div className="flex h-full">
            <Sidebar {
                ...{
                    handleClick: handleClick,
                    current_content: current_content
                }
            } />
                {children}
        </div>
        <Footer/>
    </div> );
}

export default DefaultLayout;


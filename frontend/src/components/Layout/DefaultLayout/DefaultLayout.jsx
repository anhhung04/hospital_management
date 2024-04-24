import Header from "./Header";
import Sidebar from "./SideBar";
import Footer from "./Footer";
import { useState } from "react";
import PropTypes from 'prop-types';
import apiCall from "../../../utils/api";

DefaultLayout.propTypes = {
    children: PropTypes.node,
};

function DefaultLayout({children}) {

    const [isLogin, setIsLogin] = useState(false);
    // This function gets the value of a named cookie
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
      }


    function verifyToken() {
        const access_token = getCookie('access_token');
        if (!access_token) {
          // console.log('No access token found');
          return;
        }
       
        apiCall({
            endpoint: "/api/auth/verify",
            method: "POST",
            requestData: { access_token: access_token },
        })
        .then(data => {
          console.log('Data:', data);
            if(data.data.is_login === true){
                setIsLogin(true);
            }else{
                setIsLogin(false);
            }
            // console.log('isLogin:', isLogin);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
      }

      // Call verifyToken when the page loads
      verifyToken();

    const [current_content, setCurrent_content] = useState("general");  
    function handleClick(content) {
        setCurrent_content(content);
    }
    // console.log('isLogin:', isLogin);
    return (<div className="flex flex-col h-full w-full justify-between mb-0">
        <Header isLogin={isLogin}/>
        <div className="flex flex-row">
            <Sidebar current_content={current_content} handleClick={handleClick} isLogin={isLogin}/>
                {children}
        </div>
        <Footer/>
    </div> );
}


export default DefaultLayout;


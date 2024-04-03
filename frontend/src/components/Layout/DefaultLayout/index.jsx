import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./SideBar";
import { useState } from "react";

function DefaultLayout({children}) {

    const [isLogin, setIsLogin] = useState(false);


    // This function gets the value of a named cookie
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
      }

    function setCookie(name, value, seconds) {
      let expires = "";
      if (seconds) {
          const date = new Date();
          date.setTime(date.getTime() + (seconds* 1000));
          expires = "; expires=" + date.toUTCString();
      }
      document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }
      

    function verifyToken() {
        const access_token = getCookie('access_token');
        if (!access_token) {
          console.log('No access token found');
          return;
        }
        console.log('Access token found:', access_token);
        fetch('/api/auth/verify', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ access_token: access_token })
        })
        .then(response => response.json())
        .then(data => {
            if(data.data.isLogin === true){
                setIsLogin(true);
                const newToken = "" 
                const SecondsToRefresh = 30; 
                setCookie('access_token', newToken, SecondsToRefresh);
            }else{
                setIsLogin(false);
            }
            console.log('isLogin:', isLogin);
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


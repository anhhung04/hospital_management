import { useNavigate, useLocation } from "react-router-dom";
import PropTypes from 'prop-types';
import DropDown from "../../DropDown";
import { useState } from "react";
import ChangePassword from "../../ChangePassword";

Header.propTypes = {
  isLogin: PropTypes.bool,
};

function Header(props) {
  const navigate = useNavigate();
  const location = useLocation();
  const [showChangePassword, setShowChangePassword] = useState(false);

  function setChangePassword(){
    setShowChangePassword(true);
  }

  function closeChangePassword(){
    setShowChangePassword(false);
  }

  

  const isLoginRoute = location.pathname === "/login";

  // console.log("isLogin1111", props.isLogin);
  return (
    <header className="flex w-full px-[49px] py-[35px]  items-center justify-center bg-[#FBFBFC] border-solid  border-[2px] shadow-md h-[130px]">
      {showChangePassword && <ChangePassword closeChangePassword={closeChangePassword}/>}
      <div className="flex items-center justify-between gap-[60em] w-full h-[56px] ">
        <div className="h-[56px] w-[112px] flex flex-col injustify-center items-center ">
          <img src="/images/image.png" alt="logo" onClick={()=>navigate('/')} className=""/>
        </div>
        {(isLoginRoute || !props.isLogin) ? (<h5 className="font-sans w-[136px] h-[36px] font-semibold text-[24px]  text-[#032B91] hover:text-[#6E7F94]" onClick={()=> navigate('/login')}>
          Đăng Nhập
          </h5>):(<div className="w-[109px] h-[45px] flex items-center justify-end gap-[30px]">
              <button className="w-[32px] h-[32px] flex justify-center items-center"><img src="/images/header_ring.png" alt="ring ring ring" className="hover:size-7"/></button>
              <DropDown  setChangePassword={setChangePassword}/>
          </div>)}
      </div>
    </header>
  );
}

export default Header;
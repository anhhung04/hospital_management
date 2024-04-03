import { useNavigate, useLocation } from "react-router-dom";
import PropTypes from 'prop-types';

Header.propTypes = {
  isLogin: PropTypes.bool,
};

function Header(props) {
  const navigate = useNavigate();
  const location = useLocation();

  const isLoginRoute = location.pathname === "/login";

  console.log("isLogin1111", props.isLogin);
  return (
    <header className="flex w-full px-[49px] py-[35px]  items-center justify-center bg-[#FBFBFC] border-solid  border-[2px] shadow-md h-[130px]">
      <div className="flex items-center justify-between gap-[60em] w-full h-[56px] ">
        <div className="h-[56px] w-[112px] flex flex-col injustify-center items-center ">
          <img src="/images/image.png" alt="logo" onClick={()=>navigate('/')} className=""/>
        </div>
        {(isLoginRoute || !props.isLogin) ? (<h5 className="font-sans w-[136px] h-[36px] font-semibold text-[24px]  text-[#032B91] hover:text-[#6E7F94]" onClick={()=> navigate('/login')}>
          Đăng Nhập
          </h5>):(<div className="w-[200px] h-[56px] flex items-center gap-[30px]">
              <div className="w-[32px] h-[32px] flex justify-center items-center"><img src="/images/header_ring.png" alt="ring ring ring" className="hover:size-8"/></div>
              <div className="w-[42px] h-[42px] flex justify-center items-center"><img src="/images/header_button.png" alt="ring ring ring" className="hover:size-[40px]" /></div>
              <div className="w-[35px] h-[35px]"><img src="/images/People_Icon.png" alt="People" /></div>
          </div>)}
           
      </div>
    </header>
  );
}

export default Header;
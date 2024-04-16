import { useState } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from 'prop-types';

DropDown.propTypes = {
  setChangePassword: PropTypes.func,
};

function DropDown(props) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  const handleChangePasswordClick = () => {
    if (props.setChangePassword) {
      props.setChangePassword(); // Assuming it's a function. Add parameters if needed.
    }
    closeMenu(); // Corrected function call
  };

  function eraseCookie(name) {
    document.cookie = name + '=; Max-Age=-99999999;';
  }

  const navigate = useNavigate();

  return (
    <>
      <div className="w-[50px] h-[50px] relative inline-block">
        <button onClick={toggleMenu} className="w-[50px] h-[50px]">
          <img
            src="/images/People_Icon.png"
            alt="People"
            className=" w-[45px] h-[45px] hover:h-[47px] hover:w-[47px]"
          />
        </button>

        {isMenuOpen && (
          <div
            className="absolute right-0 z-10 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
            role="menu"
            aria-orientation="vertical"
            aria-labelledby="menu-button"
            tabIndex="-1"
          >
            <div className="py-1" role="none">
              <button
                className="text-gray-700 w-full flex px-4 py-2 text-sm"
                role="menuitem"
                tabIndex="-1"
                id="menu-item-0"
                onClick={handleChangePasswordClick}
              >
                Đổi mật khẩu
              </button>
              <button
                className="text-gray-700 w-full flex px-4 py-2 text-sm"
                role="menuitem"
                tabIndex="-1"
                id="menu-item-0"
                onClick={() => {navigate('/login'); eraseCookie('access_token')}}
              >
                Đăng xuất
              </button>
              {/* <form method="POST" action="#" role="none">
              <button type="submit" className="text-gray-700 block w-full px-4 py-2 text-left text-sm" role="menuitem" tabIndex="-1" id="menu-item-3">Sign out</button>
            </form> */}
            </div>
          </div>
        )}
      </div>
    </>
  );
}

export default DropDown;

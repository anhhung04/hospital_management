import { useState } from "react";
import Alert from "./Alert";
import PropTypes from 'prop-types';

ChangePassword.propTypes = {
  closeChangePassword: PropTypes.func,
};


function ChangePassword(props) {
  const [isHiddenOldPassword, setIsHiddenOldPassword] = useState(true);
  const [isHiddenNew1Password, setIsHiddenNew1Password] = useState(true);
  const [isHiddenNew2Password, setIsHiddenNew2Password] = useState(true);
  const [oldPassword, setOldPassword] = useState("");
  const [new1Password, setNew1Password] = useState("");
  const [new2Password, setNew2Password] = useState("");
  const [isAlert, setIsAlert] = useState(false);
  const [successAlert, setSuccessAlert] = useState(false);
  const [failAlert, setFailAlert] = useState(false);

  function toggleHiddenOldPassword() {
    setIsHiddenOldPassword(pre => !pre);
  }

  function toggleHiddenNew1Password() {
    setIsHiddenNew1Password(pre => !pre);
  }

  function toggleHiddenNew2Password() {
    setIsHiddenNew2Password(pre => !pre);
  }

  function closeAlert() {
    setIsAlert(false);
  }

  function closeSuccessAlert() {
    setSuccessAlert(false);
  }

  function closeFailAlert() {
    setFailAlert(false);
  }


  function handleClickSave() {
    if (new1Password !== new2Password) {
      setIsAlert(true);
    } else {
        fetch("/api/auth/password/change", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            "old_password": oldPassword,
            "new_password": new1Password,
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.status === 200) {
              setSuccessAlert(true);
            } else {
              setFailAlert(true);
            }
          })
          .catch((error) => console.error("Error:", error));
  }
  }

  return (
    <>
      <div
        className="fixed inset-0 z-50 overflow-y-auto "
        aria-labelledby="modal-title"
        role="dialog"
        aria-modal="true"
      >
        <div className="flex items-center justify-center min-h-screen ">
          <div className="relative w-full max-w-md p-4 mx-auto bg-[#FAFBFF] rounded-[50px] shadow-lg">
            <div className="p-4 flex flex-col justify-center items-center">
              <img src="/images/lock.png" alt="lock" className="mt-[20px]" />
              <div className="w-full h-[50px] flex justify-center items-center">
                <h3 className="text-[30px] font-sans font-semibold">
                  Change Password
                </h3>
              </div>
              <div className="flex items-center gap-[4px] self-stretch">
                <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000]">
                  Mật khẩu cũ
                </h6>
                <h6 className="inline-block text-[#f00] font-sans text-[20px] font-medium leading-[32px]">
                  *
                </h6>
              </div>
              <div className="w-full h-[48px] flex justify-end items-center relative">
                <input
                  type={isHiddenOldPassword ? "password" : "text"}
                  className="w-full h-[40px] flex gap-[8px] self-stretch rounded-[5px] border-solid border-[1px] "
                  placeholder="************"
                  onChange={(e) => {
                    setOldPassword(e.target.value);
                    // resetLoginFailed();
                  }}
                  // onKeyDown={handleKeyDown}
                  // disabled={isDisabled}
                />
                <button className="absolute mr-[10px]" onClick={toggleHiddenOldPassword}>
                {isHiddenOldPassword ? (
                  <img
                    src="/images/Login_HiddenPassword.png"
                    alt="Search Icon"
                  />
                ) : (
                  <img src="/images/Login_SeePassword.png" alt="Search Icon" />
                )}
                </button>
              </div>
              <div className="flex items-center gap-[4px] self-stretch">
                <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000]">
                  Mật khẩu mới
                </h6>
                <h6 className="inline-block text-[#f00] font-sans text-[20px] font-medium leading-[32px]">
                  *
                </h6>
              </div>
              <div className="w-full h-[48px] flex justify-end items-center relative">
                <input
                  type={isHiddenNew1Password ? "password" : "text"}
                  className="w-full h-[40px] flex gap-[8px] self-stretch rounded-[5px] border-solid border-[1px] "
                  placeholder="************"
                  onChange={(e) => {
                    setNew1Password(e.target.value);
                    // resetLoginFailed();
                  }}
                  // onKeyDown={handleKeyDown}
                  // disabled={isDisabled}
                />
                <button className="absolute mr-[10px]" onClick={toggleHiddenNew1Password}>
                {isHiddenNew1Password ? (
                  <img
                    src="/images/Login_HiddenPassword.png"
                    alt="Search Icon"
                  />
                ) : (
                  <img src="/images/Login_SeePassword.png" alt="Search Icon" />
                )}
                </button>
              </div>


              <div className="flex items-center gap-[4px] self-stretch">
                <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000]">
                  Nhập lại mật khẩu
                </h6>
                <h6 className="inline-block text-[#f00] font-sans text-[20px] font-medium leading-[32px]">
                  *
                </h6>
              </div>
              <div className="w-full h-[48px] flex justify-end items-center relative">
                <input
                  type={isHiddenNew2Password ? "password" : "text"}
                  className="w-full h-[40px] flex gap-[8px] self-stretch rounded-[5px] border-solid border-[1px] "
                  placeholder="************"
                  onChange={(e) => {
                    setNew2Password(e.target.value);
                    // resetLoginFailed();
                  }}
                  // onKeyDown={handleKeyDown}
                  // disabled={isDisabled}
                />
                <button className="absolute mr-[10px]" onClick={toggleHiddenNew2Password}>
                {isHiddenNew2Password ? (
                  <img
                    src="/images/Login_HiddenPassword.png"
                    alt="Search Icon"
                  />
                ) : (
                  <img src="/images/Login_SeePassword.png" alt="Search Icon" />
                )}
                </button>
              </div>
              {isAlert && (
          <Alert
            message="Mật khẩu mới không khớp"
            isAlert={isAlert}
            closeAlert={closeAlert}
            icon_type="warning"
          />
        )}
        {successAlert && (
          <Alert
            message="Đổi mật khẩu thành công"
            isAlert={successAlert}
            closeAlert={closeSuccessAlert}
            icon_type="success"
          />
        )}
        {failAlert && (
          <Alert
            message="Mật khẩu cũ không đúng"
            isAlert={failAlert}
            closeAlert={closeFailAlert}
            icon_type="error"
          />
        )}
            </div>
            <div className="flex justify-end p-4 border-t">
              <button
                type="button"
                onClick={props.closeChangePassword}
                className="px-6 py-2 text-sm font-medium uppercase bg-gray-100 text-primary-700 rounded hover:bg-gray-200 focus:outline-none"
              >
                Close
              </button>
              <button
                type="button"
                className="ml-2 px-6 py-2 text-sm font-medium uppercase bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none"
                onClick={handleClickSave}
              >
                Save changes
              </button>
            </div>
          </div>
        </div>
      </div>
      
    </>
  );
}

export default ChangePassword;

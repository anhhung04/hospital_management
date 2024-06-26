import { useState } from "react";
import { useNavigate } from "react-router-dom";
import apiCall from "../utils/api"
import Alert from "../components/Alert";

function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isDisabled, setDisabled] = useState(false);
  const [isAlert, setAlert] = useState(false);
  const [alertMessage, setAlertMessage] = useState("");
  const [isLoginFailed, setLoginFailed] = useState(false);
  const [isForget, setIsForget] = useState(false);
  const [isHidden, setIsHidden] = useState(true);


  const handleData = (data) => {
    // console.log("success", data);
    if (data.status_code === 200) {
      console.log("accessToken", data.data.access_token);
      document.cookie = `access_token=${data.data.access_token};max-age=0.5;path=/`;
      navigate("/");
    } else {
      setDisabled(false);
      // alert("Sai tên đăng nhập hoặc mật khẩu");
      // console.log(data.message);
      setAlertMessage(data.message);
      setAlert(true);
      setLoginFailed(true);
      // console.log(data.status_code);
      // console.log(isAlert);
      // console.log(alertMessage);
      // console.log("isDisabled",isDisabled)
    }
  };

  const resetLoginFailed = () => {
    if (isLoginFailed) {
      setLoginFailed(false);
    }
  };

  const submitForm = async () => {
    setDisabled(true);
    const data = {
      username: username,
      password: password,
    };

    PostData(data);

    // console.log("username", username);
    // console.log("password", password);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      // console.log("Enter key pressed!");
      submitForm();
    }
  };

  function PostData(userData) {
      apiCall({
        endpoint: "/api/auth/login",
        method: "POST",
        requestData: userData,
      }).then((data) => {
        handleData(data);
      });
  }

  function closeAlert() {
    setAlert(false);
  }

  function closeForget() {
    setIsForget(false);
  }

  function toggleHidden() {
    setIsHidden((pre) => !pre);
  }

  return (
    <>
      <div className="w-full h-screen bg-[#EFF7FE] flex justify-center items-center ">
        <div className="bg-[#FFFF] relative flex flex-col justify-center gap-[4px] rounded-[30px] shadow-2xl w-[613px] h-[80.226%] p-[40px]">
          <div className="flex justify-center items-center gap-[10px] p-[10px] self-stretch mb-[24px]">
            <h3 className="font-sans text-[48px] font-medium leading-[72px]">
              {" "}
              Đăng Nhập
            </h3>
          </div>
          <div className="flex items-center mt-0 self-stretch">
            <h6 className="font-sans text-[20px] font-medium leading-[32px]">
              Tên đăng nhập
            </h6>
            <h6 className="inline-block text-[#f00] font-sans text-[20px] font-medium leading-[32px]">
              *
            </h6>
          </div>
          <input
            type="text"
            className="flex py-[12px] px-[8px] self-stretch rounded-[5px] border-solid border-[1px] mb-[20px]"
            placeholder="Nguyễn Văn A"
            onChange={(e) => {
              setUsername(e.target.value);
              resetLoginFailed();
            }}
            onKeyDown={handleKeyDown}
            disabled={isDisabled}
          />
          <div className="flex flex-col items-start">
            <div className="flex items-center gap-[4px] self-stretch">
              <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000]">
                Mật khẩu
              </h6>
              <h6 className="inline-block text-[#f00] font-sans text-[20px] font-medium leading-[32px]">
                *
              </h6>
            </div>
            <div className="w-full h-[48px] flex justify-end items-center relative">
              <input
                type={isHidden ? "password" : "text"}
                className="w-full flex gap-[8px] self-stretch rounded-[5px] border-solid border-[1px] "
                placeholder="************"
                onChange={(e) => {
                  setPassword(e.target.value);
                  resetLoginFailed();
                }}
                onKeyDown={handleKeyDown}
                disabled={isDisabled}
              />
              <button className="absolute mr-[10px]" onClick={toggleHidden}>
                {isHidden ? (
                  <img
                    src="/images/Login_HiddenPassword.png"
                    alt="Search Icon"
                  />
                ) : (
                  <img src="/images/Login_SeePassword.png" alt="Search Icon" />
                )}
              </button>
            </div>

            <div className="flex flex-row mt-[20px] items-end w-[200px] h-[16px]">
              <input type="checkbox" className="bg-[#DBEEFC] mr-[5px]" />
              <h6 className="font-sans text-[13px] font-medium align-text-bottom text-[#000]">
                Ghi nhớ tài khoản
              </h6>
            </div>
            <div className="flex flex-col items-center self-stretch mt-6">
              <div className="flex p-[10px] flex-col justify-center items-center gap-[10px] self-stretch">
                <button
                  className="flex w-[200px] h-[52px] justify-center items-center gap-[10px] rounded-2xl bg-[#032B91] font-sans text-[24px] font-semibold leading-[36px] text-center text-[#F9FBFF]"
                  onClick={submitForm}
                >
                  Đăng nhập
                </button>
              </div>
              <div className="flex justify-center items-center p-[10px] gap-[10px] self-stretch ">
                <span className="font-sans text-[20px] leading-[32px] font-medium text-[#000]">
                  Quên{" "}
                </span>
                <button onClick={() => setIsForget(true)}>
                  <span className="font-sans text-[20px] leading-[32px] font-medium text-[#0544E4] hover:text-[#6E7F94]">
                    Tên đăng nhập | mật khẩu
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>

        {isAlert && (
          <Alert
            message={alertMessage}
            isAlert={isAlert}
            closeAlert={closeAlert}
            icon_type="error"
          />
        )}
        {isForget && (
          <Alert
            message="Vui lòng liên hệ quản trị viên để biết tên đăng nhập hoặc mật khẩu."
            isAlert={isForget}
            closeAlert={closeForget}
            icon_type="warning"
          />
        )}
      </div>
    </>
  );
}

export default Login;

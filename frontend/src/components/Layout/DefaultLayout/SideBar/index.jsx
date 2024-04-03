import { useNavigate } from "react-router-dom";
import Alert from "../../../Alert";
import { useState } from "react";

const content_nav = {
  general: {
    name: "Tổng quát",
    path: "/",
  },
  patient: {
    name: "Bệnh nhân",
    path: "/patient",
  },
  staff: {
    name: "Nhân viên",
    path: "/employee",
  },
  medicine: {
    name: "Thuốc",
    path: "/medicine",
  },
  equipment: {
    name: "Thiết bị",
    path: "/equipment",
  },
};

function Sidebar(props) {
  const navigate = useNavigate();

  function renderBackground(current_content, contentName) {
    if (current_content === contentName) {
      return "bg-[#021B5C]";
    } else {
      return "";
    }
  }

  const [isAlert, setAlert] = useState(false);

  return (
    <>
    {isAlert && ( <Alert
                   message= "Vui lòng đăng nhập để xem chi tiết thông tin"
                    isAlert= {true}
                    icon_type="warning"
                    closeAlert={() => setAlert(false)}
                />)}
    <div className="w-[210px] h-full bg-[#032B91] border-[2px] border-solid border-black shadow-blue-600">
      <div className="w-[174px] h-[358px] mt-[40px] mx-[18px] mb-[934px] inline-flex flex-col gap-[40px]">
        {Object.keys(content_nav).map((contentKey) => (
          <div
            key={contentKey} 
            className={`w-[174px] h-[40px] flex-shrink-0 rounded-full hover:bg-[#021B5C] hover:opacity-40 hover:text-[#FFF] flex justify-center items-center ${renderBackground(
              props.current_content,
              contentKey
            )}`}
            onClick={() => {
              if(props.isLogin === false && contentKey !== 'general'){
                // <Alert
                //   message= "Bạn cần đăng nhập để sử dụng chức năng này!"
                //   isAlert= {true}
                //   icon_type="error"
                // />
                setAlert(true);
              }
              // }else{
              //   navigate(content_nav[contentKey].path);
              //   props.handleClick(contentKey);
              // }
              if(props.isLogin === true){
                navigate(content_nav[contentKey].path);
                props.handleClick(contentKey);
              }
              
            }}
          >
            <h4 className="text-[#FFF] truncate hover:text-clip font-sans text-[20px] font-medium leading-[32px]">
              {content_nav[contentKey].name}
            </h4>
          </div>
        ))}
      </div>
    </div>
    </>
  );
}

export default Sidebar;

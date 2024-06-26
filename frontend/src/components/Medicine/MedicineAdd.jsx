import InfoMedicine from "./InfoMedicine";
import { useState } from "react";
// import ProgressContent from "../Patients/PatientsAdd/ProgressContent";
// import PatientContent from "../Patients/PatientsAdd/PatientContent";
// import ResultContent from "../Patients/PatientsAdd/ResultContent";
// import MedicineContent from "../Patients/PatientsAdd/MedicineContent";
import HuyButton from "../Button/Huy_Button";
import LuuButton from "../Button/Luu_Button";
import Alert from "../Alert";
import PropTypes from "prop-types";
import WareHouse from "./WareHouse";
import UsingMedicine from "./UsingMedicine";
MedicineAdd.propTypes = {
  isStore: PropTypes.bool,
  closeAlert: PropTypes.func,
  CloseAdd: PropTypes.func,
  setStore: PropTypes.func,
};

function MedicineAdd(props) {
  const [current_content, setCurrent_content] = useState("info");

  const [isAdd, setIsAdd] = useState(false);

  const [isAddResult, setIsAddResult] = useState(false);

  // const [isAddMedicine, setIsAddMedicine] = useState(false);

  var [numStaffAdded, setNumStaffAdded] = useState(0);

  // var [numMedicineAdded, setNumMedicineAdded] = useState(0);

  // const [isFinishInfo, setIsFinishInfo] = useState(false);
  // const [isAlertWarning, setIsAlertWarning] = useState(false);
  const [isSuccesAlert, setIsSuccesAlert] = useState(false);

  // const [isPostSubmit, setIsPostSubmit] = useState(false);
  // const [isPatientSubmit, setIsPatientSubmit] = useState(false);
  const [isProgressSubmit, setIsProgressSubmit] = useState(false);
  const [isSubmitFailed, setIsSubmitFailed] = useState(false);

  // const [resDataInfo, setResDataInfo] = useState({
  //   status_code: 500,
  //   data: {},
  // });

  // function getDataInfo(res_data) {
  //   // console.log("res_data:",res_data);
  //   // console.log("resDataInfo:",resDataInfo);
  //   if (res_data.status_code === 200) {
  //     // console.log("resDataInfo",resDataInfo);
  //     setResDataInfo(res_data);
  //     props.setStore();
  //     //setIsFinishInfo(true);
  //     document.cookie = `user_id=${res_data.data.user_id};max-age=0.5;path=/`;
  //   } else if (resDataInfo.status_code === 500) {
  //     setIsSubmitFailed(true);
  //   }
  // }

  function getDataProgress(res_data) {
    // console.log("res_data11111111111111111:",res_data);
    if (res_data.status_code === 200) {
      // console.log("resDataInfo");
      setIsSuccesAlert(true);
    } else {
      setIsSubmitFailed(true);
    }
  }

  // function getDataPatient(res_data) {
  //   // console.log("res_data11111111111111111:",res_data);
  //   if (res_data.status_code === 200) {
  //     // console.log("resDataInfo");
  //     setIsSuccesAlert(true);
  //   } else {
  //     setIsSubmitFailed(true);
  //   }
  // }

  function setAdd() {
    setIsAdd((pre) => !pre);
  }

  function setAddResult() {
    setIsAddResult((pre) => !pre);
  }

  // function setAddMedicine() {
  //   setIsAddMedicine((pre) => !pre);
  // }

  // function handleNumMedicineAdded() {
  //   // console.log("click");
  //   setNumMedicineAdded((pre) => pre + 1);
  // }

  // function closeWarningAlert() {
  //   setIsAlertWarning(false);
  // }

  function closeSuccesAlert() {
    if (current_content === "info") {
      props.closeAlert();
     // setIsPostSubmit(false);
      setCurrent_content("patient");
    } else if (current_content === "patient") {
      setIsSuccesAlert(false);
      //setIsPatientSubmit(false);
      setCurrent_content("progress");
    } else if (current_content === "progress") {
      setIsSuccesAlert(false);
      setIsProgressSubmit(false);
    }
  }

  function closeSubmitFailed() {
    if (current_content === "info") {
      //setIsPostSubmit(false);
      setIsSubmitFailed(false);
    } else if (current_content === "patient") {
      //setIsPatientSubmit(false);
      setIsSubmitFailed(false);
    } else if (current_content === "progress") {
      setIsProgressSubmit(false);
      setIsSubmitFailed(false);
    }
  }

  // function handleSubmitFailed() {
  //   setIsSubmitFailed(true);
  // }

  // function handleNumMedicineRemove() {
  //   setNumMedicineAdded((pre) => pre - 1);
  // }

  function handleClick(content, key_content) {
    if (key_content === content) {
      return "bg-[#032B91]";
    } else {
      return "";
    }
  }

  function handleSubmit() {
    if (current_content === "info") {
      // console.log("info page");
      //setIsPostSubmit(true);
    } else if (current_content === "patient") {
      // console.log("patient page");
      //setIsPatientSubmit(true);
    } else if (current_content === "progress") {
      setIsProgressSubmit(true);
    }
  }

  function handleClickText(content, key_content) {
    if (key_content === content) {
      return "text-[#F9FBFF]";
    } else {
      return "text-[#032B91]";
    }
  }
  function handleClickAddStaff() {
    setNumStaffAdded((pre) => pre + 1);
  }

  function handleClickRemoveStaff() {
    setNumStaffAdded((pre) => pre - 1);
  }

  // let dynamicHeight = 1270 + numStaffAdded * 88;

  // let dynamicHeightMedicine = 1146 + numMedicineAdded * 88;

  function handleContainer(content) {
    let heightStyle = {};

    if (content === "info" || content === "patient") {
      heightStyle = { height: "609px" };
    } else if (
      content === "progress" ||
      content === "result" ||
      content === "medicine"
    ) {
      heightStyle = { height: "609px" };
    }
    return heightStyle;
  }
  return (
    <>
      {props.isStore && (
        <Alert
          message={`Thêm kết quả mới được thêm thành công`}
          icon_type="success"
          closeAlert={closeSuccesAlert}
          type="Lưu thành công"
        />
      )}
      {/* {isAlertWarning && (
        <Alert
          message={`Bạn cần phải điền thông tin bệnh nhân trước khi điền thông tin bệnh án`}
          icon_type="warning"
          closeAlert={closeWarningAlert}
          type="Cảnh báo"
        />
      )} */}
      {isSuccesAlert && (
        <Alert
          message={`Cập nhật thông tin bệnh án thành công`}
          icon_type="success"
          closeAlert={closeSuccesAlert}
          type="Thành công"
        />
      )}

      {isSubmitFailed && (
        <Alert
          message="Thông tin không hợp lệ vui vòng điền lại"
          icon_type="error"
          closeAlert={closeSubmitFailed}
          type="Lưu không thành công"
        />
      )}
      <div
        className={` w-[1087x] my-[5%] inline-flex flex-col justify-center items-end gap-[20px] `}
      >
        <div className="w-[1080px] h-[48px] px-[36px] flex justify-end items-center gap-[712px] ">
          <div className="w-[251px] h-[48px] flex justify-center items-center">
            <p className="text-[#032B91] font-sans text-[34px] font-semibold leading-[48px]">
              Loại thuốc mới
            </p>
          </div>
          <button>
            <img
              src="/images/Alert_exit_button.png"
              alt="exit button"
              onClick={props.CloseAdd}
            />
          </button>
        </div>
        <div
          style={handleContainer(
            current_content
          )}
          className="w-[1080px] flex flex-col items-center bg-[#FFF] rounded-[50px] shadow-xl"
        >
          <div className="w-[1080px] h-[79px] flex flex-col items-center justify-center gap-[10px] bg-[#CDDBFE] rounded-t-[50px]">
            <div className="w-[949px] h-[52px] flex items-center gap-[200px]  ">
              <div
                className={`w-[300px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "info"
                )}`}
                onClick={() => setCurrent_content("info")}
              >
                <p
                  className={`w-full text-center text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[10px] py-[8px] ${handleClickText(
                    current_content,
                    "info"
                  )}`}
                >
                  Thông tin
                </p>
              </div>
              <div
                className={`w-[300px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "patient"
                )}`}
                onClick={() => {
                  setCurrent_content("patient")
                }}
              >
                <p
                  className={`w-full text-center text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[10px] py-[8px] ${handleClickText(
                    current_content,
                    "patient"
                  )}`}
                >
                  Nhập kho
                </p>
              </div>
              <div
                className={`w-[300px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "progress"
                )}`}
                onClick={() => {
                  setCurrent_content("progress")
                }}
              >
                <p
                  className={`w-full text-center text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[10px] py-[8px] ${handleClickText(
                    current_content,
                    "progress"
                  )}`}
                >
                  Lượt sử dụng
                </p>
              </div>
              {/* <div
                className={`w-[172px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "result"
                )}`}
                onClick={() => {
                  isFinishInfo
                    ? setCurrent_content("result")
                    : setIsAlertWarning(true);
                }}
              >
                <p
                  className={`text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[31px] py-[8px] ${handleClickText(
                    current_content,
                    "result"
                  )}`}
                >
                  Kết quả
                </p>
              </div>
              <div
                className={`w-[172px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "medicine"
                )}`}
                onClick={() => {
                  isFinishInfo
                    ? setCurrent_content("medicine")
                    : setIsAlertWarning(true);
                }}
              >
                <p
                  className={`text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[27px] py-[8px] ${handleClickText(
                    current_content,
                    "medicine"
                  )}`}
                >
                  Đơn thuốc
                </p>
              </div> */}
            </div>
          </div>
          {current_content === "info" && (
            <InfoMedicine
              setAdd={setAdd}
              isAdd={isAdd}
              addStaff={handleClickAddStaff}
              removeStaffAdded={handleClickRemoveStaff}
              numStaffAdded={numStaffAdded}
              isProgressSubmit={isProgressSubmit}
              getDataProgress={getDataProgress}
            />
          )}
          {current_content === "patient" && (
            <WareHouse
            setAddResult={setAddResult}
            isAddResult={isAddResult}
          />
          )}
          {current_content === "progress" && (
            <UsingMedicine
            setAddResult={setAddResult}
            isAddResult={isAddResult}
          />
          )}
        </div>
        <div className="w-[330px] h-[52px] flex px-[36px] items-start gap-[18px] ">
          <div onClick={props.CloseAdd}>
            <HuyButton />
          </div>

          <div onClick={handleSubmit}>
            <LuuButton />
          </div>
        </div>
      </div>
    </>
  );
}

export default MedicineAdd;

import InfoContent from "./InfoContent";
import { useState } from "react";
import ProgressContent from "./ProgressContent";
import PatientContent from "./PatientContent";
import ResultContent from "./ResultContent";
import MedicineContent from "./MedicineContent";
import HuyButton from "../../Button/Huy_Button";
import LuuButton from "../../Button/Luu_Button";
import Alert from "../../Alert";
import PropTypes from 'prop-types';

PatientAdd.propTypes = {
    isStore: PropTypes.bool,
    closeAlert: PropTypes.func,
    CloseAdd: PropTypes.func,
    setStore: PropTypes.func,
};

function PatientAdd(props) {
  const [current_content, setCurrent_content] = useState("info");

  const [isAdd, setIsAdd] = useState(false);

  const [isAddResult, setIsAddResult] = useState(false);

  const [isAddMedicine, setIsAddMedicine] = useState(false);

  var [numStaffAdded, setNumStaffAdded] = useState(0);

  var [numMedicineAdded, setNumMedicineAdded] = useState(0);

  function setAdd() {
    setIsAdd((pre) => !pre);
  }

  function setAddResult() {
    setIsAddResult((pre) => !pre);
  }

  function setAddMedicine() {
    setIsAddMedicine((pre) => !pre);
  }

  function handleNumMedicineAdded() {
    console.log("click");
    setNumMedicineAdded((pre) => pre + 1);
  }

  function handleNumMedicineRemove() {
    setNumMedicineAdded((pre) => pre - 1);
  }

  function handleClick(content, key_content) {
    if (key_content === content) {
      return "bg-[#032B91]";
    } else {
      return "";
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

  let dynamicHeight = 1270 + numStaffAdded * 88;

  let dynamicHeightMedicine = 1146 + numMedicineAdded * 88;

  function handleContainer(content, dynamicHeight, dynamicHeightMedicine) {
    let heightStyle = {};

    if (content === "info" || content === "patient") {
      heightStyle = { height: "915px" };
    } else if (content === "progress" && isAdd) {
      heightStyle = { height: `${dynamicHeight}px` };
    } else if (content === "medicine" && isAddMedicine) {
      heightStyle = { height: `${dynamicHeightMedicine}px` };
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
          message="Thêm kết quả mới được thêm thành công"
          icon_type="success"
          closeAlert={props.closeAlert}
          type="Lưu thành công"
        />
      )}
      <div
        className={` w-[1087x] my-[5%] inline-flex flex-col justify-center items-end gap-[20px] `}
      >
        <div className="w-[1080px] h-[48px] px-[36px] flex justify-end items-center gap-[712px] ">
          <div className="w-[251px] h-[48px] flex justify-center items-center">
            <p className="text-[#032B91] font-sans text-[34px] font-semibold leading-[48px]">
              Bệnh nhân mới
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
          style={handleContainer(current_content, dynamicHeight, dynamicHeightMedicine)}
          className="w-[1080px] flex flex-col items-center bg-[#FFF] rounded-[50px] shadow-xl"
        >
          <div className="w-[1080px] h-[79px] flex flex-col items-center justify-center gap-[10px] bg-[#CDDBFE] rounded-t-[50px]">
            <div className="w-[949px] h-[52px] flex items-center gap-[26px]  ">
              <div
                className={`w-[172px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "info"
                )}`}
                onClick={() => setCurrent_content("info")}
              >
                <p
                  className={`text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[31px] py-[8px] ${handleClickText(
                    current_content,
                    "info"
                  )}`}
                >
                  Thông tin
                </p>
              </div>
              <div
                className={`w-[172px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "patient"
                )}`}
                onClick={() => setCurrent_content("patient")}
              >
                <p
                  className={`text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[31px] py-[8px] ${handleClickText(
                    current_content,
                    "patient"
                  )}`}
                >
                  Bệnh án
                </p>
              </div>
              <div
                className={`w-[172px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "progress"
                )}`}
                onClick={() => setCurrent_content("progress")}
              >
                <p
                  className={`text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[31px] py-[8px] ${handleClickText(
                    current_content,
                    "progress"
                  )}`}
                >
                  Tiến trình
                </p>
              </div>
              <div
                className={`w-[172px] h-[52px] flex justify-center items-center hover:bg-[#032B91] rounded-[50px] ${handleClick(
                  current_content,
                  "result"
                )}`}
                onClick={() => setCurrent_content("result")}
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
                onClick={() => setCurrent_content("medicine")}
              >
                <p
                  className={`text-[24px] font-semibold leading-[36px] hover:text-[#F9FBFF] px-[27px] py-[8px] ${handleClickText(
                    current_content,
                    "medicine"
                  )}`}
                >
                  Đơn thuốc
                </p>
              </div>
            </div>
          </div>
          {current_content === "info" && <InfoContent />}
          {current_content === "patient" && <PatientContent />}
          {current_content === "progress" && (
            <ProgressContent
              setAdd={setAdd}
              isAdd={isAdd}
              addStaff={handleClickAddStaff}
              removeStaffAdded={handleClickRemoveStaff}
              numStaffAdded={numStaffAdded}
            />
          )}
          {current_content === "result" && (
            <ResultContent
              setAddResult={setAddResult}
              isAddResult={isAddResult}
            />
          )}
          {current_content === "medicine" && (
            <MedicineContent
              isAddMedicine={isAddMedicine}
              setAddMedicine={setAddMedicine}
              handleNumMedicineAdded={handleNumMedicineAdded}
              handleNumMedicineRemove={handleNumMedicineRemove}
              numMedicineAdded={numMedicineAdded}
            />
          )}
        </div>
        <div className="w-[330px] h-[52px] flex px-[36px] items-start gap-[18px] ">
          <div onClick={props.CloseAdd}>
            <HuyButton />
          </div>

          <div onClick={props.setStore}>
            <LuuButton />
          </div>
        </div>
      </div>
    </>
  );
}

export default PatientAdd;

import TableList from "../TableList";
import Shortcurt from "../Shortcurt";
import PatientAdd from "./PatientsAdd/PatientsAdd";
import apiCall from "../../utils/api";


import { useEffect, useState } from "react";

function PatientsList() {

  const [checkedState, setCheckedState] = useState([]);

  const [listPatient_Info, setListPatient_Info] = useState([])

  const [isAdd, setIsAdd] = useState(false);

  const [isCheckedAll, setIsCheckedAll] = useState(false);

  const [isStore, setIsStore] = useState(false);

  function closeAlert() {
    setIsStore(false);
  }

  function setStore() {
    setIsStore(true);
  }


  useEffect(() => {
    apiCall({
      endpoint: "/api/patient/list",
      method: "GET",
    })
      .then((data) => {
        console.log("Mydata",data)
        setListPatient_Info(data.data);
        setCheckedState(new Array(data.length).fill(false));
      })
      .catch((error) => console.error('Error fetching patient data:', error));
  }, []);

  function handleClick() {
      setIsAdd(true);
  }

  function handleCheckAll() {
    setIsCheckedAll(prev => !prev);
    setCheckedState(checkedState.map(() => !isCheckedAll));
}

  function handleCheckboxChange(position) {
    const updatedCheckedState = checkedState.map((item, index) =>
        index === position ? !item : item
    );
    setCheckedState(updatedCheckedState);
    const isAllChecked = updatedCheckedState.every(Boolean);
    setIsCheckedAll(isAllChecked);
}

  if(!isAdd){
    return (
        <div className="w-full bg-[#EFF7FE] flex justify-center items-center ">
          <div className="h-[1116px] w-[1080px] flex flex-col items-start gap-[40px]">
            <Shortcurt
              title="Bệnh nhân"
              value={listPatient_Info.length}
              source="/images/Patient_HeartRateMonitor.png"
            />
  
            <TableList handleClick={handleClick} handleCheckedAll = {handleCheckAll} >
              <div className="w-[1032px] h-[716px] inline-flex flex-col items-start gap-[12px]">
                {listPatient_Info.map((info, index) => (
                  <div
                    key={index}
                    className="w-[1032px] h-[44px] flex items-center gap-[12px] bg-[#EFF7FE] py-[10px] px-[20px]"
                  >
                    <input
                      type="checkbox"
                      checked={checkedState[index]}  
                      onChange={() => handleCheckboxChange(index)}  
                    />
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[43px] h-[24px] text-right ">
                      {index}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[116px] h-[24px] text-right">
                      {info.medical_record_id}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[150px] h-[24px] text-right">
                      {info.full_name}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[125px] h-[24px] text-right">
                      {info.phone_number}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[130px] h-[24px] text-right">
                      {info.date}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[146px] h-[24px] text-right">
                      {info.time}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[150px] h-[24px] text-right">
                      Hồ sơ ↗
                    </p>
                  </div>
                ))}
              </div>
            </TableList>
          </div>
        </div>
    );
  }else{
    return(
      <div className="w-full bg-[#EFF7FE] flex justify-center items-center ">
        <PatientAdd  CloseAdd={()=>setIsAdd(false)} setStore={setStore} closeAlert={closeAlert} isStore={isStore} />
      </div>
    )
  }
  
}

export default PatientsList;

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

  const [currentpage, setCurrentPage] = useState(1);

  const [checkedCount, setCheckedCount] = useState(0);

  function closeAlert() {
    setIsStore(false);
  }

  function setStore() {
    setIsStore(true);
  }
  
  console.log("currentpage",currentpage)
  useEffect(() => {
    apiCall({
      endpoint: `/api/patient/list?page=${currentpage}&limit=13`,
      method: "GET",
    })
      .then((data) => {
        console.log("Mydata",data)
        if(data && data?.data && data.data?.length > 0){
          setListPatient_Info(data.data);
          setCheckedState(new Array(data.data.length).fill(false));
        }
      })
      .catch((error) => console.error('Error fetching patient data:', error));
  }, [currentpage]);

  function handleClick() {
      setIsAdd(true);
  }

  function handleCheckAll() {
    setIsCheckedAll(prev => !prev);
    setCheckedState(checkedState.map(() => !isCheckedAll));
    if(isCheckedAll){
      setCheckedCount(0);}
    else{
      setCheckedCount(13);
    }
}

function checkedTrue(value) {
  return value === true;
}

  function handleCheckboxChange(position) {
    const updatedCheckedState = checkedState.map((item, index) =>
        index === position ? !item : item
    );
    // if(isCheckedAll){
    //   setCheckedCount(13);
    // }
    setCheckedState(updatedCheckedState);
    const isAllChecked = updatedCheckedState.every(Boolean);
    setIsCheckedAll(isAllChecked);

    const count = updatedCheckedState.filter(checkedTrue).length;
    setCheckedCount(count);
}

console.log("checkedCount",checkedCount)

  if(!isAdd){
    return (
        <div className="w-full bg-[#EFF7FE] flex justify-center items-center ">
          <div className="h-[1116px] w-[1080px] flex flex-col items-start gap-[40px]">
            <Shortcurt
              title="Bệnh nhân"
              value={listPatient_Info.length}
              source="/images/Patient_HeartRateMonitor.png"
            />
  
            <TableList handleClick={handleClick} handleCheckedAll = {handleCheckAll} isCheckedAll={isCheckedAll} activeButton={currentpage} setActiveButton={setCurrentPage} checkedCount={checkedCount} >
              <div className="w-[1032px] h-[716px] inline-flex flex-col items-start gap-[12px]">
                {listPatient_Info.length!=0&&listPatient_Info.map((info, index) => (
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
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[80px] h-[24px] text-right">
                      {info.medical_record_id}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[200px] h-[24px] text-center">
                      {info.full_name}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[125px] h-[24px] text-left">
                      {info.phone_number}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[100px] h-[24px] text-right">
                      {info.appointment_date}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[100px] h-[24px] text-right">
                      {info.time}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[190px] h-[24px] text-right">
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

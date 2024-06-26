
import Shortcurt from "../Shortcurt";
import MedicineAdd from "./MedicineAdd";
import apiCall from "../../utils/api";
import PatientDetail from "../Patients/PatientsAdd/PatientDetail";
import TableListMedicine from "./TableListMedicine";

import { useEffect, useState } from "react";


const list_Medicine_Info = [
  { 
    medicine_id: "#00001",
    medicine_name: "Paracetamol",
    size_medicine: 1000,
    HSD: "2024-12-30",
    Date_of_manufacture: "2022-12-30",
  },
  { 
    medicine_id: "#00002",
    medicine_name: "Ibuprofen",
    size_medicine: 200,
    HSD: "2025-01-15",
    Date_of_manufacture: "2023-01-15",
  },
  { 
    medicine_id: "#00003",
    medicine_name: "Aspirin",
    size_medicine: 500,
    HSD: "2023-11-20",
    Date_of_manufacture: "2021-11-20",
  },
  { 
    medicine_id: "#00004",
    medicine_name: "Cetirizine",
    size_medicine: 10,
    HSD: "2024-08-25",
    Date_of_manufacture: "2022-08-25",
  },
  { 
    medicine_id: "#00005",
    medicine_name: "Amoxicillin",
    size_medicine: 250,
    HSD: "2023-07-14",
    Date_of_manufacture: "2021-07-14",
  },
  { 
    medicine_id: "#00006",
    medicine_name: "Metformin",
    size_medicine: 500,
    HSD: "2024-03-30",
    Date_of_manufacture: "2022-03-30",
  },
  { 
    medicine_id: "#00007",
    medicine_name: "Lisinopril",
    size_medicine: 20,
    HSD: "2025-10-10",
    Date_of_manufacture: "2023-10-10",
  },
  { 
    medicine_id: "#00008",
    medicine_name: "Omeprazole",
    size_medicine: 40,
    HSD: "2023-05-05",
    Date_of_manufacture: "2021-05-05",
  },
  { 
    medicine_id: "#00009",
    medicine_name: "Atorvastatin",
    size_medicine: 80,
    HSD: "2024-09-12",
    Date_of_manufacture: "2022-09-12",
  },
  { 
    medicine_id: "#00010",
    medicine_name: "Simvastatin",
    size_medicine: 40,
    HSD: "2023-04-22",
    Date_of_manufacture: "2021-04-22",
  },
  { 
    medicine_id: "#00011",
    medicine_name: "Levothyroxine",
    size_medicine: 100,
    HSD: "2024-02-18",
    Date_of_manufacture: "2022-02-18",
  },
  { 
    medicine_id: "#00012",
    medicine_name: "Clopidogrel",
    size_medicine: 75,
    HSD: "2023-06-30",
    Date_of_manufacture: "2021-06-30",
  },
  { 
    medicine_id: "#00013",
    medicine_name: "Pantoprazole",
    size_medicine: 20,
    HSD: "2024-01-01",
    Date_of_manufacture: "2022-01-01",
  }
];


function MedicineList() {

  const [checkedState, setCheckedState] = useState([]);

  const [listPatient_Info, setListPatient_Info] = useState([])

  const [isAdd, setIsAdd] = useState(false);

  const [isCheckedAll, setIsCheckedAll] = useState(false);

  const [isStore, setIsStore] = useState(false);

  const [currentpage, setCurrentPage] = useState(1);

  const [checkedCount, setCheckedCount] = useState(0);
  
  const [isdetail, setIsDetail] = useState(false);

  const [currentUser_id, setCurrentUser_id] = useState("");

  // const [list_Delete, setlist_Delete] = useState([]);

  // const [isSubmitDelete, setIsSubmitDelete] = useState(false);

  function closeAlert() {
    setIsStore(false);
  }

  function setStore() {
    setIsStore(true);
  }
  
  //console.log("currentpage",currentpage)
  useEffect(() => {
    apiCall({
      endpoint: `/api/patient/list?page=${currentpage}&limit=13`,
      method: "GET",
    })
      .then((data) => {
        // console.log("Mydata",data)
        if(data && data?.data && data.data?.length > 0){
          setListPatient_Info(data.data);
          setCheckedState(new Array(data.data.length).fill(false));
        }
      })
      .catch((error) => console.error('Error fetching patient data:', error));
  }, [currentpage]);

  // useEffect(() => {
  //   console.log("list_Delete state", list_Delete);
  //   for (let i = 0; i < list_Delete.length; i++) {
  //     apiCall({
  //       endpoint: `/api/patient/delete/${list_Delete[i].id}`,
  //       method: "DELETE",
  //     })
  //       .then((data) => {
  //         console.log("Mydata", data);
  //         if (data && data?.data && data.data?.length > 0) {
  //           setListPatient_Info(data.data);
  //           setCheckedState(new Array(data.data.length).fill(false));
  //         }
  //       })
  //       .catch((error) => console.error("Error fetching patient data:", error));
  //   }
  //   setIsSubmitDelete(false);
  // }, [isSubmitDelete]);
  
  // console.log("isSubmitDelete",isSubmitDelete)

  function handleClick() {
      setIsAdd(true);
  }

  function handleCheckAll() {
    setIsCheckedAll(prev => !prev);
    
    setCheckedState(checkedState.map(() => !isCheckedAll));
  //   const info_patient_selected = listPatient_Info.filter((item, index) =>
  //     (isCheckedAll===false)
  // );
  // setlist_Delete(info_patient_selected);
  // console.log("info_patient_selected state",list_Delete)
  // console.log("info_patient_selected",info_patient_selected)

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
  //   const info_patient_selected = listPatient_Info.filter((item, index) =>
  //     (updatedCheckedState[index] === true||isAllChecked===true)
  // );
  // setlist_Delete(info_patient_selected);
  // console.log("info_patient_selected state",list_Delete)
  // console.log("info_patient_selected",info_patient_selected)
    const count = updatedCheckedState.filter(checkedTrue).length;
    setCheckedCount(count);

}


//console.log("checkedCount",checkedCount)
// console.log("user_id",currentUser_id)
  if(!isAdd&&!isdetail){
    return (
        <div className="w-full bg-[#EFF7FE] flex justify-center items-center ">
          <div className="h-[1116px] w-[1080px] flex flex-col items-start gap-[40px]">
            <Shortcurt
              title="Thuốc"
              value={listPatient_Info.length}
              source="/images/Pills.png"
            />

            <TableListMedicine handleClick={handleClick} handleCheckedAll = {handleCheckAll} isCheckedAll={isCheckedAll} activeButton={currentpage} setActiveButton={setCurrentPage} checkedCount={checkedCount}>
            <div className="w-[1032px] h-[716px] inline-flex flex-col items-start gap-[12px]">
                {list_Medicine_Info.length!=0&&list_Medicine_Info.map((info, index) => (
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
                      {info.medicine_id}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[150px] h-[24px] text-center">
                      {info.medicine_name}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[80px] h-[24px] text-right">
                      {info.size_medicine}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[130px] h-[24px] text-right">
                      {info.HSD}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[190px] h-[24px] text-right">
                      {info.Date_of_manufacture}
                    </p>
                    <p className="font-sans text-[16px] font-normal leading-[24px] w-[150px] h-[24px] text-right text-[#0544E4]" onClick={()=>{setIsDetail(true);setCurrentUser_id(info.id)}}>
                      Hồ sơ ↗
                    </p>
                  </div>
                ))}
              </div>
            </TableListMedicine>
  
            {/* <TableListMedicine  >
             
            </TableListMedicine> */}
          </div>
        </div>
    );
  }else if(isdetail){
    return(
      <div className="w-full bg-[#EFF7FE] flex justify-center items-center ">
        <PatientDetail  CloseAdd={()=>setIsDetail(false)} setStore={setStore} closeAlert={closeAlert} isStore={isStore} user_id={currentUser_id} />
      </div>
    )
  }
  else{
    return(
      <div className="w-full bg-[#EFF7FE] flex justify-center items-center ">
        <MedicineAdd  CloseAdd={()=>setIsAdd(false)} setStore={setStore} closeAlert={closeAlert} isStore={isStore} />
      </div>
    )
  }
  
}

export default MedicineList;

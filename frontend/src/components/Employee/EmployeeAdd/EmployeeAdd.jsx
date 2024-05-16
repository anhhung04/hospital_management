import { useEffect, useState, useRef } from "react";

import apiCall from "../../../utils/api";
import HuyButton from "../../Button/Huy_Button";
import LuuButton from "../../Button/Luu_Button";

import AddInfo from "./AddInfo";
import AddSpecialist from "./AddSpecialist";
import AddSchedule from "./AddSchedule";
import AddPatient from "./AddPatient";
import NotiPopup from "../Component/NotiPopup";


function EmployeeAdd({handleCloseAdd, handleAddDone, viewEmp, viewEmpId}) {
    const [content, setContent] = useState('info');
    const infoButtonRef = useRef(null);
    const specialistButtonRef = useRef(null);
    const scheduleButtonRef = useRef(null);
    const patientButtonRef = useRef(null);
    const [showNotiPopup, setShowNotiPopup] = useState(false);
    const [dataDone, setDataDone] = useState(false);
    const [submitStatus, setSubmitStatus] = useState("success");
    const [empInfo, setEmpInfo] = useState({});
    const [currentEmp, setCurrentEmp] = useState({});
    const [update, setUpdate] = useState(false);
    const [updateEmp, setUpdateEmp] = useState({});


    const [newEmpInfo, setNewEmpInfo] = useState({
        first_name: null,
        last_name: null,
        birth_date: null,
        gender: null,
        ssn: null,
        phone_number: null,
        address: null,
        email: null,
        health_insurance: null,
        employee_type: null
    });

    useEffect(() => {
        if (dataDone) {
            apiCall({
                endpoint: "/api/employee/create",
                method: "POST",
                requestData: newEmpInfo,
            }).then((res) => {
                console.log(res);
                if (res.status_code !== 200) {
                    handleSubmitFail();
                }
                else {
                    handleSubmitSuccess();
                }
            }).catch((error) => console.error('Error employee data format:', error));
            ;
        }
    }, [dataDone]);

    useEffect(() => {
        if (viewEmp && update) {
            apiCall({
                endpoint: `/api/employee/${viewEmpId}/update`,
                method: "PATCH",
                requestData: updateEmp,
            }).then((res) => {
                console.log("update employee", res);
                if (res.status_code !== 200) {
                    handleSubmitFail();
                }
                else {
                    handleSubmitSuccess();
                }
            }).catch((error) => console.error('Error employee data format:', error));
            ;
        }
    }, [update]);

    useEffect(() => {
        setUpdate(false);
        if (viewEmp) {
            apiCall({
                endpoint: `/api/employee/${viewEmpId}`,
                method: "GET",
              })
                .then((data) => {
                  console.log("My employee info",data)
                  if(data && data?.data){
                    setEmpInfo(data.data);
                    updateCurrentEmp(data.data);
                  }
                  else {    
                    setEmpInfo({});
                    setCurrentEmp({});
                  }
                })
                .catch((error) => console.error('Error fetching employee data:', error));
        }
    }, [update]);

    const updateCurrentEmp = (data) => {
        setCurrentEmp({
            education_level: data.education_level,
            begin_date: data.begin_date,
            end_date: data.end_date,
            faculty: data.faculty,
            personal_info: {
              phone_number: data.personal_info.phone_number,
              birth_date: data.personal_info.birth_date,
              gender: data.personal_info.gender,
              health_insurance: data.personal_info.health_insurance,
              last_name: data.personal_info.last_name,
              first_name: data.personal_info.first_name,
              address: data.personal_info.address
            }
        })

    }

    const handleSubmitFail = () => {
        console.log("SUBMIT FAIL");
        if (!viewEmp) {
            setDataDone(false);
        }
        setSubmitStatus("fail");
        setShowNotiPopup(true);
    }

    const handleSubmitSuccess = () => {
        console.log("SUBMIT SUCCESS");
        if (!viewEmp) {
            setDataDone(true);
        }
        setSubmitStatus("success");
        setShowNotiPopup(true);
    }
    const handleOpenNotiPopup = () => {
        if (content === "schedule" || content === "patient" || content === "specialist") setSubmitStatus("alert");
        setShowNotiPopup(true);
    }

    
    const handleCloseNotiPopup = () => {
        setShowNotiPopup(false);
        if(viewEmp) {
            setUpdate(false);
        }
    }

    const handleAlertClose = () => {
        if (['last_name', 'first_name', 'birth_date', 'gender', 'ssn', 'phone_number', 'address', 'employee_type', 'email'].every(field => newEmpInfo[field] === null || newEmpInfo[field] === "")) {
            handleCloseAdd();
        }
        else {
            setSubmitStatus("warning");
            handleOpenNotiPopup();
        }
    }

    const handleSave = () => {
        if (content === "info") {
            if (['last_name', 'first_name', 'birth_date', 'gender', 'ssn', 'phone_number', 'address', 'employee_type', 'email'].every(field => newEmpInfo[field] !== null && newEmpInfo[field] !== "")) {
                setSubmitStatus("success");
                setDataDone(true);
            }
            else {
                setSubmitStatus("fail");
                setDataDone(false);
                handleOpenNotiPopup();
            }
        }

    }

    const handleChangeValue = (field, value) => {
        if (!viewEmp) {
            if (field === "degree") {
                const updatedDegree = newEmpInfo.degree;
                updatedDegree[parseInt(value[0])] = value.substr(1);
                setNewEmpInfo({ ...newEmpInfo, degree: updatedDegree });
            }
            else setNewEmpInfo({...newEmpInfo, [field]: value});
        }
        else {
            if (["education_level", "begin_date", "end_date", "faculty", "status"].includes(field)) {
                setCurrentEmp({ ...currentEmp, [field]: value });
                setUpdateEmp({...updateEmp, [field]: value});
            } else {
                setCurrentEmp({
                    ...currentEmp,
                    personal_info: {
                        ...currentEmp.personal_info,
                        [field]: value
                    }
                });
                setUpdateEmp({
                    ...updateEmp,
                    personal_info: {
                        ...updateEmp.personal_info,
                        [field]: value
                    }
                });
            }            
        }

    }

    const handleRemoveDegree = (value) => {
        const updatedDegree = newEmpInfo.degree.filter(deg => deg !== value);
        setNewEmpInfo({ ...newEmpInfo, degree: updatedDegree });
    }
    
    const handleChangeTab = (tab) => {
        if (viewEmp) {
            setContent(tab);
        }
        else {
            if(tab !== "info") {
                setSubmitStatus("alert");
                setShowNotiPopup(true);
            }
            else setContent("info");
        }
    }

    console.log(currentEmp);


    return (
        <div className="w-full bg-[#EFF7FE] flex items-center flex-col">
            {
                showNotiPopup &&
                <div className="fixed inset-0 z-[1] flex items-center justify-center bg-black bg-opacity-50">
                    <div className="relative z-[2]">
                        <NotiPopup content = {submitStatus} page = {content} done = {dataDone} handleCloseNotiPopup={handleCloseNotiPopup} handleAddDone = {handleAddDone} handleCloseAdd = {handleCloseAdd} viewEmp={viewEmp}/>
                    </div>
                </div>
            }
            <div className="top-section mt-[8px] w-[1080px] px-[36px] py-[20px] flex items-center justify-between">
                <div className="content flex items-center">
                    <p className="text-[#032B91] text-[32px] font-bold leading-[48px]">
                        {viewEmp? empInfo?.personal_info?.last_name + " " + empInfo?.personal_info?.first_name : "Nhân viên mới"}
                    </p>
                </div>
                <button className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid"
                    onClick={handleAlertClose}>
                    <img src="/images/xbutton.png"/>
                </button>
            </div>
            <div className="table-container w-[1080px] h-fit rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
                <div className="w-[1080px] h-[76px] bg-[#CDDBFE] rounded-t-[47px] flex justify-between px-[36px] items-center">
                    <button className={` ${content === "info"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="info" onClick={() => handleChangeTab("info")} ref={infoButtonRef}>Thông tin</button>
                    <button className={` ${content === "specialist"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="specialist" onClick={() => handleChangeTab("specialist")} ref={specialistButtonRef}>Chuyên môn</button>
                    <button className={` ${content === "schedule"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="schedule" onClick={() => handleChangeTab("schedule")} ref={scheduleButtonRef}>Lịch làm việc</button>
                    <button className={` ${content === "patient"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="patient" onClick={() => handleChangeTab("patient")} ref={patientButtonRef}>Bệnh nhân</button>
                </div>
                <div className="content">
                    {content === 'info' && <AddInfo handleChangeValue = {handleChangeValue} empInfo = {empInfo} currentEmp = {currentEmp} viewEmp = {viewEmp}/>}
                    {content === 'specialist' && <AddSpecialist handleChangeValue = {handleChangeValue} handleRemoveDegree = {handleRemoveDegree} empInfo = {empInfo} currentEmp = {currentEmp} viewEmp = {viewEmp}/>}
                    {content === 'schedule' && <AddSchedule handleOpenNoti = {handleOpenNotiPopup} empId = {viewEmpId}/>}
                    {content === 'patient' && <AddPatient empId = {viewEmpId}/>}

                </div>
           </div>
           <div className="footer-section w-[1080px] mt-[20px] pr-[36px] flex justify-end">
                <div className="pr-[18px]" onClick={handleAlertClose}>
                    <HuyButton/>
                </div>
                <div className="hover:cursor-pointer" onClick={() => {viewEmp? setUpdate(true) : handleSave()}}>
                    <LuuButton/>
                </div>
           </div>
        </div>
    )
}

export default EmployeeAdd;
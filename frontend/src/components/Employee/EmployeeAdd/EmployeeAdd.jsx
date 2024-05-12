import { useEffect, useState, useRef } from "react";
import HuyButton from "../../Button/Huy_Button";
import LuuButton from "../../Button/Luu_Button";

import AddInfo from "./AddInfo";
import AddSpecialist from "./AddSpecialist";
import AddSchedule from "./AddSchedule";
import AddPatient from "./AddPatient";
import NotiPopup from "../Component/NotiPopup";


function EmployeeAdd({handleCloseAdd, handleAddDone}) {
    const [content, setContent] = useState('info');
    const infoButtonRef = useRef(null);
    const specialistButtonRef = useRef(null);
    const scheduleButtonRef = useRef(null);
    const patientButtonRef = useRef(null);
    const [showNotiPopup, setShowNotiPopup] = useState(false);
    const [dataDone, setDataDone] = useState(false);
    const [submitStatus, setSubmitStatus] = useState("success");

    const [newEmpInfo, setNewEmpInfo] = useState({
        name: "abc",
        imgURL: null,
        last_name: null,
        first_name: null,
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
            fetch("/api/employees", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(newEmpInfo),
            })
            .then((response) => response.json())
            .then((data) => {
                console.log("Employee created:", data);
            })
            .catch((error) => console.error('Error creating employee:', error));
        }
    }, [dataDone]);

    const handleOpenNotiPopup = () => {
        if (content === "schedule" || content === "patient" || content === "specialist") setSubmitStatus("alert");
        setShowNotiPopup(true);
    }

    
    const handleCloseNotiPopup = () => {
        setShowNotiPopup(false);
    }

    const handleAlertClose = () => {
        if (['last_name', 'first_ame', 'birth_date', 'gender', 'ssn', 'phone_number', 'address', 'employee_type', 'eamil'].every(field => newEmpInfo[field] === null || newEmpInfo[field] === "")) {
            handleCloseAdd();
        }
        else {
            setSubmitStatus("warning");
            handleOpenNotiPopup();
        }
    }

    const handleSaveTest = () => {
        if (content === "info") {
            if (['last_name', 'first_name', 'birth_date', 'gender', 'ssn', 'phone_number', 'address', 'employee_type', 'email'].every(field => newEmpInfo[field] !== null && newEmpInfo[field] !== "")) {
                setSubmitStatus("success");
                setDataDone(true);
            }
            else {
                setSubmitStatus("fail");
                setDataDone(false);
            }
            
        }
        // if (content === "specialist") {
        //     if (['type', 'faculty', 'position', 'jobTitle', 'dateBegin'].every(field => newEmpInfo[field] !== null && newEmpInfo[field] !== "")) {
        //         setSubmitStatus("success");
        //         if (['lastName', 'firstName', 'dob', 'gender', 'ssn', 'phone', 'address'].every(field => newEmpInfo[field] !== null && newEmpInfo[field] !== "")) {
        //             const filteredDegreeArray = newEmpInfo.degree.filter(deg => deg !== "");
        //             setNewEmpInfo(prevState => ({
        //             ...prevState,
        //             degree: filteredDegreeArray
        //     }));
        //             setDataDone(true);
        //         }
        //         else {
        //             setDataDone(false);
        //         }
        //     }
        //     else {
        //         setSubmitStatus("fail");
        //     }
        // }
        handleOpenNotiPopup();
        console.log(newEmpInfo);
    }

    const handleChangeValue = (field, value) => {
        if (field === "degree") {
            const updatedDegree = newEmpInfo.degree;
            updatedDegree[parseInt(value[0])] = value.substr(1);
            setNewEmpInfo({ ...newEmpInfo, degree: updatedDegree });
        }
        else setNewEmpInfo({...newEmpInfo, [field]: value});
    }

    const handleRemoveDegree = (value) => {
        const updatedDegree = newEmpInfo.degree.filter(deg => deg !== value);
        setNewEmpInfo({ ...newEmpInfo, degree: updatedDegree });
    }
    
    return (
        <div className="w-full bg-[#EFF7FE] flex items-center flex-col">
            {
                showNotiPopup &&
                <div className="fixed z-[1] left-[33%] top-[28%]">
                    <NotiPopup content = {submitStatus} page = {content} done = {dataDone} handleCloseNotiPopup={handleCloseNotiPopup} handleAddDone = {handleAddDone} handleCloseAdd = {handleCloseAdd}/>
                </div>
            }
            <div className="top-section mt-[8px] w-[1080px] px-[36px] py-[20px] flex items-center justify-between">
                <div className="content flex items-center">
                    <p className="text-[#032B91] text-[32px] font-bold leading-[48px]">Nhân viên mới</p>
                </div>
                <button className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid"
                    onClick={handleAlertClose}>
                    <img src="/images/xbutton.png"/>
                </button>
            </div>
            <div className="table-container w-[1080px] h-fit rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
                <div className="w-[1080px] h-[76px] bg-[#CDDBFE] rounded-t-[47px] flex justify-between px-[36px] items-center">
                    <button className={` ${content === "info"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="info" onClick={() => setContent("info")} ref={infoButtonRef}>Thông tin</button>
                    <button className={` ${content === "specialist"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="specialist" onClick={() => setContent("specialist")} ref={specialistButtonRef}>Chuyên môn</button>
                    <button className={` ${content === "schedule"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="schedule" onClick={() => setContent("schedule")} ref={scheduleButtonRef}>Lịch làm việc</button>
                    <button className={` ${content === "patient"? "bg-[#032B91] text-[#F9FBFF] font-semibold" : "text-[#032B91] font-bold"} w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="patient" onClick={() => setContent("patient")} ref={patientButtonRef}>Bệnh nhân</button>
                </div>
                <div className="content">
                    {content === 'info' && <AddInfo handleChangeValue = {handleChangeValue}/>}
                    {content === 'specialist' && <AddSpecialist handleChangeValue = {handleChangeValue} handleRemoveDegree = {handleRemoveDegree}/>}
                    {content === 'schedule' && <AddSchedule handleOpenNoti = {handleOpenNotiPopup}/>}
                    {content === 'patient' && <AddPatient handleOpenNoti={handleOpenNotiPopup}/>}

                </div>
           </div>
           <div className="footer-section w-[1080px] mt-[20px] pr-[36px] flex justify-end">
                <div className="pr-[18px]" onClick={handleAlertClose}>
                    <HuyButton/>
                </div>
                <div className="hover:cursor-pointer" onClick={handleSaveTest}>
                    <LuuButton/>
                </div>
           </div>
        </div>
    )
}

export default EmployeeAdd;
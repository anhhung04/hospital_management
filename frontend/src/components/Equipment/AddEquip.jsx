import HuyButton from "../Button/Huy_Button";
import LuuButton from "../Button/Luu_Button";
import { useState, useEffect } from 'react';
import apiCall from "../../utils/api";
import NotiPopup from "./NotiPopup";
import PropTypes from 'prop-types';

AddEquip.propTypes = {
    viewEquip: PropTypes.bool,
    viewEquipId: PropTypes.string,
    handleAddDone: PropTypes.func,
    equipInfo: PropTypes.shape ({
        name: PropTypes.string,
        status: PropTypes.string,
        maintanance_history: PropTypes.string,
        availability: PropTypes.bool,
        description: PropTypes.string,
    })
};


function AddEquip({viewEquip, viewEquipId, handleAddDone, equipInfo}) {
    const [showNotiPopup, setShowNotiPopup] = useState(false);
    const [newEquipInfo, setNewEquipInfo] = useState({
            name: "",
            availability: true,
            maintanance_history: "",
            description: "",
            status: "",
            quantity: 0
    })

    const [dataDone, setDataDone] = useState(false);
    const [submitStatus, setSubmitStatus] = useState("success");

    console.log("view Emp Id", viewEquipId);
    console.log("view Emp", viewEquip);



    const handleChangeValue = (field, value) => {
        if (!viewEquip) {
            setNewEquipInfo({...newEquipInfo, [field]: value});
            console.log(newEquipInfo);
        }
    }


    useEffect(() => {
        if (dataDone) {
            apiCall({
                endpoint: "/api/equipment/create",
                method: "POST",
                requestData: newEquipInfo
            })
            .then(res => console.log("Create equipment", res))
            .catch(err => console.log("Error", err))
        }
    }, [dataDone, newEquipInfo])

    const handleSave = () => {
        if (['name', 'availability', 'maintanance_history', 'status'].every(field => newEquipInfo[field] !== null && newEquipInfo[field] !== "")) {
            setSubmitStatus("success");
            setDataDone(true);
            setShowNotiPopup(true);
        }
        else {
            setSubmitStatus("fail");
            setDataDone(false);
            setShowNotiPopup(true);
        }
    }
    const handleAlertClose = () => {
        if (['name', 'availability', 'maintanance_history', 'status'].every(field => newEquipInfo[field] === null || newEquipInfo[field] === "" || newEquipInfo[field] === true)) {
            handleAddDone();
        }
        else {
            setSubmitStatus("warning");
            setShowNotiPopup(true);
        }
    }

    return (
        <div>
            <div className="w-full bg-[#EFF7FE] flex items-center flex-col"> 
                {
                    showNotiPopup &&
                    <div className="fixed inset-0 z-[1] flex items-center justify-center bg-black bg-opacity-50">
                        <div className="relative z-[2]">
                            <NotiPopup content = {submitStatus} done = {dataDone} handleCloseNotiPopup={() => setShowNotiPopup(false)} handleAddDone = {handleAddDone}/>
                        </div>
                    </div>
                }
                <div className="top-section mt-[8px] w-[1080px] px-[36px] py-[20px] flex items-center justify-between">
                    <div className="content flex items-center">
                        <p className="text-[#032B91] text-[32px] font-bold leading-[48px]">
                            {Object.keys(equipInfo).length === 0 ? "Thiết bị mới" : equipInfo.name}
                        </p>
                    </div>
                    <button className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid"
                        onClick={handleAlertClose}>
                        <img src="/images/xbutton.png"/>
                    </button>
                </div>
                <div className="table-container w-[1080px] h-fit rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
                    <div className="w-[1080px] h-[76px] bg-[#CDDBFE] rounded-t-[47px] flex justify-between px-[36px] items-center">
                        <button className={` bg-[#032B91] text-[#F9FBFF] font-semibold w-[200px] h-[44px] text-2xl leading-9 px-5 py-1 rounded-[20px] `} id="info" >Thông tin</button>
                    </div>
                    <div className="content">
                    <form className="my-[40px]" id="myForm" encType="multipart/form-data">
                        <div className="first-section mt-[40px] flex justify-between items-center px-[60px]">
                            <div>
                                <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Tên
                                    <span className="text text-[#F00]">*</span>
                                </label><br/>
                                <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="Máy đo huyết áp" disabled={viewEquip}  onChange={(e) => handleChangeValue("name", e.target.value)} 
                                    value= {Object.keys(equipInfo).length === 0 ? null : equipInfo?.name}/><br/>
                            </div>
                            <div>
                                <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Tình trạng
                                    <span className="text text-[#F00]">*</span>
                                </label><br/>
                                <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="Tốt" disabled={viewEquip}  onChange={(e) => handleChangeValue("status", e.target.value)} 
                                    value= {Object.keys(equipInfo).length === 0 ? null : equipInfo?.status}/><br/>
                            </div>
                        </div>                                
                        <div className="second-section mt-[40px] flex justify-between items-center px-[60px]">
                            <div>
                                <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Ngày bảo dưỡng
                                    <span className="text text-[#F00]">*</span>
                                </label><br/>
                                <input className="w-[450px] rounded-[5px] mt-[4px]" type="date" id="text" name="text" placeholder="" disabled={viewEquip}  onChange={(e) => handleChangeValue("maintanance_history", e.target.value)} 
                                    value= {Object.keys(equipInfo).length === 0 ? null : equipInfo?.maintanance_history} /><br/>
                            </div>
                            <div>
                                <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Sự sẵn có
                                    <span className="text text-[#F00]">*</span>
                                </label><br/>
                                <select className="w-[450px] rounded-[5px] mt-[4px]" id="genders" name="genders" disabled={viewEquip} onChange={(e) =>  handleChangeValue("availability", e.target.value)} value= {Object.keys(equipInfo).length === 0 ? null : equipInfo?.availability}>
                                    <option value="" disabled selected>Chọn sự sẵn có</option>
                                    <option value={false}>Không có</option>
                                    <option value={true}>Có sẵn</option>
                                </select>
                            </div>
                        </div>                                
                        <div className="fifth-section mt-[40px] flex justify-between items-center px-[60px]">
                            <div>
                                <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Hướng dẫn sử dụng
                                    <span className="text text-[#F00]"></span>
                                </label><br/>
                                <input className="w-[960px] h-[100px] rounded-[5px] mt-[4px] pb-[60px]" type="text" id="text" name="text" placeholder="Theo nhà sản xuất" disabled={viewEquip} onChange={(e) => handleChangeValue("description", e.target.value)} 
                                    value= {Object.keys(equipInfo).length === 0 ? null : equipInfo?.description} /><br/>
                            </div>
                        </div>
                    </form>
                    </div>
               </div>
               {
                !viewEquip &&
                <div className="footer-section w-[1080px] mt-[20px] pr-[36px] flex justify-end">
                    <div className="pr-[18px]" onClick={handleAlertClose}>
                        <HuyButton/>
                    </div>
                    <div className="hover:cursor-pointer" onClick={handleSave}>
                        <LuuButton/>
                    </div>
                </div>
               }
               
            </div>
        </div>
    )
}

export default AddEquip;
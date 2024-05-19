import InfoTag from "../Employee/Component/InfoTag";
import ListBar from "../Employee/Component/ListBar/ListBar";
import "./style.css";
import { useEffect, useState } from "react";
import apiCall from "../../utils/api";
import NotiPopup from "../Employee/Component/NotiPopup";
import AddEquip from "./AddEquip";

function EquipmentList() {
    const [equipList, setEquipList] = useState([]);
    const [pageNumber, setPageNumber] = useState(1);
    const [addEquip, setAddEquip] = useState(false);
    const [viewEquip, setViewEquip] = useState(false);
    const [viewEquipId, setViewEquipId] = useState();
    const [equipInfo, setEquipInfo] = useState({});


    useEffect(() => {
        apiCall({
            endpoint: `/api/equipment/list?page=${pageNumber}&limit=13`,
            method: "GET"
        })
        .then((res) => {
            console.log("Equipment list", res);
            if (res && res?.data && res?.data.length > 0) {
                setEquipList(res.data);
            }
            else {
                setEquipList([]);
            }
        })
        .catch((error) => console.error('Error fetching employee data:', error));

    }, [pageNumber, addEquip])

    useEffect(() => {
        if (viewEquip) {
            apiCall({
                endpoint: `/api/equipment/${viewEquipId}`,
                method: "GET"
            })
            .then(res => {
                console.log(res);
                if (res && res?.data) {
                    setEquipInfo(res.data);
                }
                else {
                    setEquipInfo({});
                }
            })
            .catch(err => console.log("Error", err))
        }
    }, [viewEquip, viewEquipId, addEquip])


    useEffect(() => {
        if (viewEquipId) {
            setViewEquip(true);
        }
        else {
            setViewEquip(false);
        }
    }, [viewEquipId])

    console.log(equipList);

    if (!addEquip) {
        return (
            <div className="w-full bg-[#EFF7FE] flex items-center flex-col">
                <div className='flex ml-[-40px] my-[40px] w-[1080px]'>
                    <InfoTag 
                        title="Thiết bị"
                        value={equipList.length}
                        source="/images/Microscope.png"
                    ></InfoTag>
                </div>
                <div className="container w-[1080px] h-[920px] rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
                    <div className="flex justify-between mx-10 mt-7 mb-5">
                        <div className="flex items-center">
                            <button className="icon-wrapper mr-[8px]" onClick={() => setAddEquip(true)}>
                                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                                    <circle className="cir" cx="16" cy="16" r="16" fill="#EFF7FE"/>
                                    <path className="plus" fillRule="evenodd" clipRule="evenodd" d="M15 7C14.4477 7 14 7.44772 14 8V14H8C7.44772 14 7 14.4477 7 15V17C7 17.5523 7.44772 18 8 18H14V24C14 24.5523 14.4477 25 15 25H17C17.5523 25 18 24.5523 18 24V18H24C24.5523 18 25 17.5523 25 17V15C25 14.4477 24.5523 14 24 14H18V8C18 7.44772 17.5523 7 17 7H15Z" fill="#032B91"/>
                                </svg>
                            </button>
                            <p className="text-[#032B91] text-2xl font-semibold leading-9">Thiết bị</p>
                        </div>
                        <div className="right-section gap-[16px] flex items-center justify-end">
                            <div className="w-[237px] h-[42px] flex shrink-0 items-center rounded-full bg-[#EFF7FE] px-[20px] py-[12px]">
                                <div className="font-sans text-[12px] font-normal leading-[18px] text-[#000]">Tìm kiếm</div>
                            </div>
                            <img src="/images/Patient_Sorted.png" alt="sorted" />
                            <img src="/images/Patient_filter.png" alt="filter" />
                        </div>
                    </div>
                    <div className="list flex flex-col items-center justify-center mt-0">
                        <div className="w-[1008px] h-[56px] bg-[#CDDBFE] flex justify-between items-center px-[40px]">
                            <p className="text-black text-xl font-medium leading-8">STT</p>
                            <p className="text-black text-xl font-medium leading-8">Tên</p>
                            <p className="text-black text-xl font-medium leading-8">Tình trạng</p>
                            <p className="text-black text-xl font-medium leading-8">Ngày bảo dưỡng</p>
                            <p className="text-black text-xl font-medium leading-8">Sẵn có</p>
                            <p className="text-black text-xl font-medium leading-8">Chi tiết</p>
                        </div>
                    </div>
                    <div className="content mt-[18px] flex flex-col justify-start mx-[36px]">
                        {equipList.map((eq, index) => (
                            <div key={index} className="flex justify-start my-[8px]">
                                <p className="text-black font-normal leading-6 flex justify-center w-[110px]">{index + 1}</p>
                                <p className="text-black font-normal leading-6 flex justify-center w-[160px]">{eq?.name}</p>
                                <p className="text-black font-normal leading-6 flex justify-center w-[140px]">{eq?.status}</p>
                                <p className="text-black font-normal leading-6 flex justify-center w-[300px]">{eq?.maintanance_history}</p>
                                <p className="text-black font-normal leading-6 flex justify-center w-[120px]">{eq?.availability? "Có sẵn" : "Không có sẵn"}</p>
                                <p className="text-[#0544E4] font-normal leading-6 flex justify-center pl-[38px] w-[180px]" onClick={() => {setViewEquipId(eq.id); setAddEquip(true)}}>Chi tiết ↗</p>
                            </div>
                        ))}
                    </div>
                    
                </div>
                <div className='flex items-center w-[1080px] justify-between p-[10px] mt-[24px]'>
                    <div>
                        <p className='text-black text-lg font-medium leading-6'>Tổng số lượng: {equipList.length}</p>
                    </div>
                    <ListBar pageNumber={pageNumber} handlePage={(page) => setPageNumber(page)}/>
                </div>
            </div>
        )
    }
    else {
        return (
            <div className="w-full bg-[#EFF7FE] flex items-center flex-col">
                <AddEquip viewEquip = {viewEquip} viewEquipId = {viewEquipId} handleAddDone = {() => {setAddEquip(false); setViewEquipId(null)}} equipInfo={equipInfo}/>
            </div>
        )
    }

}

export default EquipmentList;
import { useState, useRef } from "react";
import "./style.css" 
import FormList from "./FormList";
import ListBar from "../../Component/ListBar/ListBar";

function AddPatient({handleOpenNoti}) {

    return (
        <div className="table-conttainer w-full px-[60px] py-[40px] ">            
            <div className="header flex justify-between items-center">
                <div className="left-header flex items-center">
                        <div className="flex items-center">
                            <button className="Add-button" onClick={handleOpenNoti}>
                                <div className="icon-wrapper">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                                        <circle className="cir" cx="16" cy="16" r="16" fill="#EFF7FE"/>
                                        <path className="plus" fillRule="evenodd" clipRule="evenodd" d="M15 7C14.4477 7 14 7.44772 14 8V14H8C7.44772 14 7 14.4477 7 15V17C7 17.5523 7.44772 18 8 18H14V24C14 24.5523 14.4477 25 15 25H17C17.5523 25 18 24.5523 18 24V18H24C24.5523 18 25 17.5523 25 17V15C25 14.4477 24.5523 14 24 14H18V8C18 7.44772 17.5523 7 17 7H15Z" fill="#032B91"/>
                                    </svg>
                                </div>
                            </button>
                        </div>
                        <div className="content px-[8px]">
                            <p className="text-[#032B91] text-2xl font-semibold leading-9">Bệnh nhân</p>
                        </div>
                </div>
                <div className="right-header gap-[16px] flex items-center content-end">
                    <div className="w-[237px] h-[42px] flex shrink-0 items-center rounded-full bg-[#EFF7FE] px-[20px] py-[12px]">
                        <div className="text-[12px] font-normal leading-[18px] text-[#000]">Tìm kiếm</div>
                    </div>
                    <img src="/images/Patient_Sorted.png" alt="sorted" />
                    <img src="/images/Patient_filter.png" alt="filter" />
                </div>

            </div>
            <div className="list my-[20px] h-[350px]">
                <FormList prop={['STT', 'Mã tiến trình', 'Bệnh nhân', 'Ngày thực hiện', 'Giờ thực hiện', 'Tình trạng', 'Chi tiết']}/>
                <div className="list-content flex flex-col justify-between items-center w-full mt-[20px]">
                    <p className="text-black text-[34px] not-italic font-medium leading-[48px] mt-[30px]">Chưa có dữ liệu nào</p>
                </div>
            </div>
        </div>
    )
}

export default AddPatient;
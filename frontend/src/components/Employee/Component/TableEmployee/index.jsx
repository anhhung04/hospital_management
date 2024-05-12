import { useState } from "react";
import React from 'react';


function TableEmployee({ children , countChecked, listLen, filterType, handleFilterType }) {
    return (
        <div className="container w-[1080px] h-[920px] rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
            <div className="flex justify-between mx-10 mt-7 mb-5">
                <div className="button-section flex">
                    <button className={`${filterType === "Tất cả"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("Tất cả")}>Tất cả</button>
                    <button className={`${filterType === "Bác sĩ"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("Bác sĩ")}>Bác sĩ</button>
                    <button className={`${filterType === "Y tá"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("Y tá")}>Y tá</button>
                    <button className={`${filterType === "Khác"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("Khác")}>Khác</button>
                </div>
                <div className="right-section gap-[16px] flex items-center justify-end">
                    {countChecked > 0 &&
                        <div className="w-[203px] h-[44px] bg-[#EFF7FE] flex shrink-0 items-center justify-center">
                            <div className="basis-full flex justify-center">
                                <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000] mx-[15px]">
                                    {countChecked === listLen ? "All Selected" : `${countChecked} Selected`}
                                </h6>
                            </div>
                            <div className="w-[60px] h-[44px] flex items-center justify-center border-l-2 border-l-[white] border-solid">
                                <img src="/images/Patient_Garbage.png" alt="icon" className="w-[24px] h-[24px]"/>
                            </div>
                        </div>
                    }
                    <div className="w-[237px] h-[42px] flex shrink-0 items-center rounded-full bg-[#EFF7FE] px-[20px] py-[12px]">
                        <div className="font-sans text-[12px] font-normal leading-[18px] text-[#000]">Tìm kiếm</div>
                    </div>
                    <img src="/images/Patient_Sorted.png" alt="sorted" />
                    <img src="/images/Patient_filter.png" alt="filter" />
                </div>
            </div>
            <div className="flex justify-center mt-0">
                <hr className="w-[1000px] border-2 border-solid border-[#A6BFFD]"/>
            </div>
            <div className="body">
                {children}
            </div>
        </div>
    )
}

export default TableEmployee;
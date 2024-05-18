function EmployeeTable() {
    return ( <>
        <div className="w-[1080px] h-[984px] inline-flex flex-col items-end gap-[26px] ">
            <div className="w-[1080px] h-[914px] bg-[#FFF] rounded-[47px] shadow-xl px-[28px] py-[40px] flex-shrink-0">
                <div className="w-full h-[44px] flex items-end justify-between ">
                    <div className="w-[429px] h-[36px] px-[20px] gap-[47px] flex flex-start">
                        <h5 className="text-[24px] font-semibold leading-[36px] text-[#032B91] ">Tất cả</h5>
                        <h5 className="text-[24px] font-semibold leading-[36px] text-[#032B91] ">Bác sĩ</h5>
                        <h5 className="text-[24px] font-semibold leading-[36px] text-[#032B91] ">Y tá</h5>
                        <h5 className="text-[24px] font-semibold leading-[36px] text-[#032B91] ">Khác</h5>
                    </div>
                    <div className="w-[552px] h-[44px] flex flex-end items-center gap-[16px]">
                    <div className="w-[203px] h-[44px] bg-[#EFF7FE] flex shrink-0 items-center justify-center rounded-full">
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000] mx-[15px]">10 Selected</h6>
                        <div className="w-[3px] h-[44px] bg-[#FFF] flex items-center justify-center"></div>
                        <div className="w-[65px] h-[44px] flex items-center justify-center">
                            <div className="w-[24px] h-[24px] flex shrink-0 items-center justify-center">
                                <img src="/images/Patient_Garbage.png" alt="icon" />
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </> );
}

export default EmployeeTable;
import PropTypes from 'prop-types';

TableEmployee.propTypes = {
    children: PropTypes.node,
    filterType: PropTypes.string,
    handleFilterType: PropTypes.func
};


function TableEmployee({ children, filterType, handleFilterType }) {
    return (
        <div className="container w-[1080px] h-[920px] rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
            <div className="flex justify-between mx-10 mt-7 mb-5">
                <div className="button-section flex">
                    <button className={`${filterType === "ALL"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("ALL")}>Tất cả</button>
                    <button className={`${filterType === "DOCTOR"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("DOCTOR")}>Bác sĩ</button>
                    <button className={`${filterType === "NURSE"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("NURSE")}>Y tá</button>
                    <button className={`${filterType === "OTHER"? "bg-[#E9EFFF] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]" : null}w-[116px] h-[44px] text-[#032B91] text-2xl font-bold leading-9 px-5 py-1 rounded-[20px]`} onClick={() => handleFilterType("OTHER")}>Khác</button>
                </div>
                <div className="right-section gap-[16px] flex items-center justify-end">
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
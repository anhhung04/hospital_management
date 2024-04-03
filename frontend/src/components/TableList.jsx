import PropTypes from 'prop-types';

TableList.propTypes = {
    children: PropTypes.node,
    handleClick: PropTypes.func,
    handleCheckedAll: PropTypes.func,
};

function TableList({children,handleClick, handleCheckedAll}) {
    return ( <div className="w-[1080px] h-[978px] inline-flex flex-col items-end gap-[26px]  ">
        <div className="flex flex-col items-center w-[1080px] h-[908px] bg-[#FFF] shadow-xl rounded-[47px] py-[28px] px-[24px]">
            <div className="w-[1032px] h-[44px] flex items-center content-center self-stretch mb-[26px] gap-[293px]">
                <div className="w-[166px] h-[36px] flex items-center gap-[6px]">
                    <button className="w-[32px] h-[32px]" onClick={handleClick}>
                        <img src="/images/Component_plus_icon.png" alt="plus_icon"  />
                    </button>
                    <div className="w-[126px] h-[36px] flex items-center gap-[10px]">
                        <h5 className="font-sans text-[24px] font-semibold leading-12 text-[#032B91]">Bệnh nhân</h5>
                    </div>
                </div>
                <div className="w-[573px] h-[44px] gap-[16px] flex items-center content-end">
                    <div className="w-[203px] h-[44px] bg-[#EFF7FE] flex shrink-0 items-center justify-center rounded-full">
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000] mx-[15px]">10 Selected</h6>
                        <div className="w-[3px] h-[44px] bg-[#FFF] flex items-center justify-center"></div>
                        <div className="w-[65px] h-[44px] flex items-center justify-center">
                            <div className="w-[24px] h-[24px] flex shrink-0 items-center justify-center">
                                <img src="/images/Patient_Garbage.png" alt="icon" />
                            </div>
                        </div>
                    </div>
                    <div className="w-[237px] h-[42px] flex shrink-0 items-center rounded-full bg-[#EFF7FE] px-[20px] py-[12px]">
                        <div className="font-sans text-[12px] font-normal leading-[18px] text-[#000]">Tìm kiếm</div>
                    </div>
                    <img src="/images/Patient_Sorted.png" alt="sorted" />
                    <img src="/images/Patient_filter.png" alt="filter" />
                </div>
            </div>
            <div className="w-[1032px] h-[56px] flex shrink-0 bg-[#CDDBFE] rounded-lg items-center justify-start mb-[20px]">
                <div className=" w-[956px] h-[32px] flex items-center gap-[19px] shrink-0 ml-[20px]">
                    <input type="checkbox"
                        onChange={handleCheckedAll}
                    />
                    <div className="flex justify-center items-end gap-[87px]">
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] ">STT</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] ">ID</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] ">Họ tên</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] ">SĐT</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] ">Ngày hẹn</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] ">Giờ hẹn</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px] ">Chi tiết</h6>
                    </div>
                </div>
            </div>
            {children}
        </div>
        <div className="w-[1080px] h-[44px] flex justify-center items-end gap-[10px] self-stretch">
            <div className="w-[858px] h-[44px] flex p-[10px] items-end gap-[10px] ">
                <p className="font-sans text-[18px] font-medium leading-[24px]">Tổng số lượng: 1</p>
            </div>
            <div className="w-[212px] h-[32px] flex justify-center items-center gap-[10px]">
                <p className="font-sans text-[20px] font-normal leading-normal text-[#BEC6CF]">←</p>
                <div className="w-[152px] h-[32px] flex items-start gap-[8px]">
                    <div className="w-[32px] h-[32px] py-[2px] px-[11px] flex flex-col justify-center items-center gap-[10px] bg-[#F9FBFF] rounded-lg shadow-lg">
                        <button className="font-sans text-[14px] font-medium leading-[24px] text-[#000]">1</button>
                    </div>
                    <div className="w-[32px] h-[32px] py-[2px] px-[11px] flex flex-col justify-center items-center gap-[10px] bg-[#F9FBFF] rounded-lg shadow-lg">
                        <button className="font-sans text-[14px] font-medium leading-[24px] text-[#000]">2</button>
                    </div>
                    <div className="w-[32px] h-[32px] py-[2px] px-[11px] flex flex-col justify-center items-center gap-[10px] bg-[#F9FBFF] rounded-lg shadow-lg">
                        <button className="font-sans text-[14px] font-medium leading-[24px] text-[#000]">3</button>
                    </div>
                    <div className="w-[32px] h-[32px] py-[2px] px-[11px] flex flex-col justify-center items-center gap-[10px] bg-[#F9FBFF] rounded-lg shadow-lg">
                        <button className="font-sans text-[14px] font-medium leading-[24px] text-[#000]">4</button>
                    </div>
                </div>
                <p className="font-sans text-[20px] font-normal leading-normal text-[#BEC6CF]">→</p>

            </div>
        </div>
    </div> );
}

export default TableList;

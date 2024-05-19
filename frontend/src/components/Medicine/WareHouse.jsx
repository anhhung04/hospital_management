import AddWareHouse from "./AddWareHouse";
import Alert from "../Alert";
import { useState } from "react";
import PropTypes from 'prop-types';

WareHouse.propTypes = {
  isAddResult: PropTypes.bool,
  setAddResult: PropTypes.func,
};

function WareHouse(props) {

  const [isSuccess, setIsSuccess] = useState(false);

  function closeAlert() {
    setIsSuccess(false);
  }

  function setSuccess() {
    setIsSuccess(true);
  }

  return (
    <>
      {!isSuccess && props.isAddResult && <AddWareHouse setAddResult={props.setAddResult} setSuccess={setSuccess} />}
      {isSuccess && <Alert message="Thêm kết quả mới được thêm thành công" icon_type="success" closeAlert={closeAlert} type="Lưu thành công" />}
      <div className="w-[960px] h-[392px] flex flex-col items-center gap-[20px] mt-[40px] mb-[99px]">
        <div className="w-[960px] h-[44px] flex items-center content-center self-stretch mb-[26px] gap-[400px]">
          <div className="w-[300px] h-[36px] flex items-center gap-[6px]">
            <button className="w-[32px] h-[32px]" onClick={props.setAddResult}>
              <img src="/images/Component_plus_icon.png" alt="plus_icon" />
            </button>
            <div className="w-[200px] h-[36px] flex items-center gap-[10px]">
              <h5 className="font-sans text-[24px] font-semibold leading-12 text-[#032B91]">
                Lần nhập kho
              </h5>
            </div>
          </div>
          <div className="w-[573px] h-[44px] gap-[16px] flex items-center content-end">
            <div className="w-[237px] h-[42px] flex shrink-0 items-center rounded-full bg-[#EFF7FE] px-[20px] py-[12px]">
              <div className="font-sans text-[12px] font-normal leading-[18px] text-[#000]">
                Tìm kiếm
              </div>
            </div>
            <img src="/images/Patient_Sorted.png" alt="sorted" />
            <img src="/images/Patient_filter.png" alt="filter" />
          </div>
        </div>
        <div className="w-[960px] h-[56px] flex shrink-0 bg-[#CDDBFE] rounded-lg items-center justify-start mb-[20px]">
          <div className=" w-[956px] h-[32px] flex items-center gap-[19px] shrink-0 ml-[20px]">
            <input
              type="checkbox"
            />
            <div className="flex justify-center items-end gap-[57px]">
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                STT
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                Mã lô hàng
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                Ngày nhập
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                SL nhập
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                SL còn lại
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                HSD
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                Chi tiết
              </h6>
            </div>
          </div>
        </div>

        <h4 className="text-[34px] font-semibold leading-[48px] ">
          Chưa có dữ liệu nào
        </h4>
      </div>
    </>
  );
}

export default WareHouse;

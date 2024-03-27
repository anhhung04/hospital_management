import AddStaff from "./components/addStaff";
import AddStaffNonHeader from "./components/addStaffNonHeader";

function ProgressContent(props) {
  return (
    <>
      <div className="w-[960px] h-[392px] flex flex-col items-center gap-[20px] mt-[40px] mb-[99px]">
        <div className="w-[960px] h-[44px] flex items-center content-center self-stretch mb-[26px] gap-[436px]">
          <div className="w-[166px] h-[36px] flex items-center gap-[6px]">
            <button className="w-[32px] h-[32px]" onClick={props.setAdd}>
              <img src="/images/Component_plus_icon.png" alt="plus_icon" />
            </button>
            <div className="w-[126px] h-[36px] flex items-center gap-[10px]">
              <h5 className="font-sans text-[24px] font-semibold leading-12 text-[#032B91]">
                Tiến trình
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
              // checked={isCheckAll}
              // onChange={toggleCheckAll}
            />
            <div className="flex justify-center items-end gap-[50px]">
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                STT
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                Mã tiến trình
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                Ngày thực hiện
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                Giờ thực hiện
              </h6>
              <h6 className="font-sans text-[20px] font-medium leading-[32px] ">
                Tình trạng
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
        {props.isAdd && (
          <div className="w-[960px] h-[56px] flex items-center content-center self-stretch mb-[26px] gap-[436px]"></div>
        )}
      </div>
      {props.isAdd && (
        <>
          <hr className="bg-[#6ABFFD] mb-[20px] border-solid w-[960px] h-[4px]" />
          <div className="h-[600px] w-[960px]">
            <h5 className="font-sans text-[24px] font-semibold leading-[36px] text-[#032B91]">
              Tiến trình mới
            </h5>
            <div className="w-full h-[544px] grid grid-cols-2 gap-x-[60px] gap-y-[40px] content-start">
              <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                  <h6 className="font-sans text-[20px] font-medium leading-[32px]">
                    Ngày thực hiện{" "}
                    <span className="text-[#F00] text-[20px] font-medium leading-8">
                      *
                    </span>
                  </h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                  <input
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]"
                    type="text"
                    placeholder="10/03/2024"
                  />
                  <img src="/images/Patient_calender.png" alt="" />
                </div>
              </div>

              <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                  <h6 className="font-sans text-[20px] font-medium leading-[32px]">
                    Giờ thực hiện{" "}
                    <span className="text-[#F00] text-[20px] font-medium leading-8">
                      *
                    </span>
                  </h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                  <input
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]"
                    type="text"
                    placeholder="10:00 AM"
                  />
                  <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
              </div>

              <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                  <h6 className="font-sans text-[20px] font-medium leading-[32px]">
                    Ngày kết thúc{" "}
                  </h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                  <input
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]"
                    type="text"
                    placeholder="10/03/2024"
                  />
                  <img src="/images/Patient_calender.png" alt="" />
                </div>
              </div>

              <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                  <h6 className="font-sans text-[20px] font-medium leading-[32px]">
                    Giờ kết thúc{" "}
                  </h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                  <input
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]"
                    type="text"
                    placeholder="10:00 PM"
                  />
                  <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
              </div>

              <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                  <h6 className="font-sans text-[20px] font-medium leading-[32px]">
                    Bệnh{" "}
                    <span className="text-[#F00] text-[20px] font-medium leading-8">
                      *
                    </span>
                  </h6>
                </div>
                <input
                  className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]"
                  type="text"
                  placeholder="Đau lưng"
                />
              </div>

              <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                  <h6 className="font-sans text-[20px] font-medium leading-[32px]">
                    Tình trạng{" "}
                    <span className="text-[#F00] text-[20px] font-medium leading-8">
                      *
                    </span>
                  </h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                  <input
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]"
                    type="text"
                    placeholder="Đã xong"
                  />
                  <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
              </div>

              <AddStaff />

              {Array.from({ length: props.numStaffAdded }, (_, index) => (
                <AddStaffNonHeader
                  key={index}
                  removeStaffAdded={props.removeStaffAdded}
                />
              ))}

              <button
                className="w-[96px] h-[48px] flex items-start gap-[11px] rounded-[5px] bg-[#EFF7FE] border-[1px] border-solid py-[12px] px-[8px]"
                onClick={props.addStaff}
              >
                <img
                  src="/images/Patient_leading_icon.png"
                  alt="leading_icon"
                />
                <h6 className="font-sans text-[16px] font-medium leading-[24px]">
                  Thêm
                </h6>
              </button>
            </div>
          </div>
        </>
      )}
    </>
  );
}

export default ProgressContent;

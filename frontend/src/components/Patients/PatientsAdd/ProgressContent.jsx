import PropTypes from "prop-types";
import { useState, useEffect, useRef } from "react";
import { Datepicker } from "flowbite-react";
import apiCall from "../../../utils/api";
import ProgressInfo from "../../ProgressInfo";
import AddStaff from "./addStaff";
import AddStaffNonHeader from "./addStaffNonHeader";

ProgressContent.propTypes = {
  isAdd: PropTypes.bool,
  setAdd: PropTypes.func,
  numStaffAdded: PropTypes.number,
  removeStaffAdded: PropTypes.func,
  addStaff: PropTypes.func,
  isProgressSubmit: PropTypes.bool,
  getDataProgress: PropTypes.func,
  progress_data: PropTypes.array,
  api_patient_id: PropTypes.string,
  setCurrentPage: PropTypes.func,
  currentpage: PropTypes.number,
  isDetailProgress: PropTypes.bool,
  setIsDetailProgress: PropTypes.func,

};

function ProgressContent(props) {
  const [date_performance, setDate_performance] = useState("");
  const [time_performance, setTime_performance] = useState("");
  const [time_finished, setTime_finished] = useState("");
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [date_finished, setDate_finished] = useState("");
  const [showDatePickerFinished, setShowDatePickerFinished] = useState(false);
  const [ishaveProgress, setIshaveProgress] = useState(false);
  const [progress, setProgress] = useState([]);
  const [objProgress, setObjProgress] = useState({});
  const [api_patient_id, setApi_patient_id] = useState("");

  function toggleDatePicker() {
    setShowDatePicker((pre) => !pre);
  }
  //console.log("progress_data", props.progress_data)
  // console.log("api_patient_id111111111", props.api_patient_id);
  useEffect(() => {
    if (props?.progress_data?.length >= 0) {
      // console.log("progress_data listtttt", props.progress_data);
      // console.log("api_patient_id", props.api_patient_id);
      // console.log("da va useeffect")
      setProgress(props.progress_data);
      setIshaveProgress(true);
      setApi_patient_id(props.api_patient_id);
    }
  },[props.progress_data, props.api_patient_id]);

  function toggleDatePickerFinished() {
    setShowDatePickerFinished((pre) => !pre);
  }

  function handleDateChange(selectedDate) {
    const month = selectedDate.getMonth() + 1; // Months are zero-based, so add 1
    const day = selectedDate.getDate();
    const year = selectedDate.getFullYear();
    setDate_performance(`${year}-${month}-${day}`);
    setObjProgress({
      ...objProgress,
      start_treatment: `${year}-${month}-${day} ${time_performance}:00`,
      date_performance: `${year}-${month}-${day}`,
    });
    setShowDatePicker(false);
  }

  function handleIncrease() {
    props.setCurrentPage(pre => pre + 1);
  }

  function handleDecrease() {
    if (props.currentpage === 1) return;
    props.setCurrentPage(pre => pre - 1);
  }

  function handleDateChangeFinished(selectedDate) {
    const month = selectedDate.getMonth() + 1; // Months are zero-based, so add 1
    const day = selectedDate.getDate();
    const year = selectedDate.getFullYear();
    setDate_finished(`${year}-${month}-${day}`);
    setObjProgress({
      ...objProgress,
      end_treatment: `${year}-${month}-${day} ${time_finished}:00`,
      date_finished: `${year}-${month}-${day}`,
    });
    setShowDatePickerFinished(false);
  }

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
  }

  useEffect(() => {
    if (!props.api_patient_id) {
      // const api_patient_id = getCookie('user_id');
      setApi_patient_id(getCookie("user_id"));
    }
  },[props.api_patient_id]);

  const progressRef = useRef(progress);
  useEffect(() => {
    progressRef.current = progress;
  }, [progress]);

  const propsRef = useRef(props.getDataProgress);

  useEffect(() => {
    propsRef.current = props.getDataProgress;
  }, [props.getDataProgress]);

  useEffect(() => {
    if (props.isProgressSubmit) {
      // console.log("objProgress", objProgress);
      apiCall({
        endpoint: `/api/patient/${api_patient_id}/progress/create`,
        method: "POST",
        requestData: objProgress,
      }).then((res_data) => {
        // console.log(res_data);
        if (res_data.status_code === 200) {
          const newprogress = [...progressRef.current, res_data.data];
          setProgress(newprogress);
          // console.log(newprogress);
          setIshaveProgress(true);
        }
        propsRef.current(res_data);
      });
    }
  }, [props.isProgressSubmit, objProgress, api_patient_id]);

  // console.log("progress", objProgress);
  // {
  //   console.log("isAdd", props.isAdd);
  // }
  // {
  //   console.log("isDetailProgress", props.isDetailProgress);
  // }

  return (
    <>
      <div className="w-[960px] h-[450px] flex flex-col gap-[20px] mt-[40px] mb-[40px] items-center justify-between">
        <div className="flex items-center flex-col gap-[20px]">
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

        {!ishaveProgress && (
          <h4 className="text-[34px] font-semibold leading-[48px] ">
            Chưa có dữ liệu nào
          </h4>
        )}
        {ishaveProgress &&
          progress.map((info, index) => (
            <ProgressInfo
              key={index}
              keyy={index}
              id={info.id}
              time={info.start_treatment}
              patient_condition={info.patient_condition}
              status={info.status}
              setIsDetail={props.setIsDetailProgress}
              setObjProgress={setObjProgress}
              detailContent={info}
            />
          ))}
        </div>

        {/* {props.isAdd && (
          <div className="w-[960px] h-[56px] flex items-center content-center self-stretch mb-[26px] gap-[436px]"></div>
        )} */}
        <div className="w-[960px] h-[32px] flex items-end gap-[26px]">
          <div className="w-[802px] px-[20px] flex gap-[10px]">
            <h3 className="font-sans text-[18px] font-medium">Tổng số lượng: {progress.length}</h3>
          </div>
          <div className="w-[92px] h-[32px] flex items-center gap-[10px]">
            <button className="font-inter text-[30px] font-medium leading-normal text-[#BEC6CF]" onClick={handleDecrease}>←</button>
            <div className="flex w-[32px] h-[32px] py-[2px] px-[11px] justify-center items-center gap-[10px] bg-[#032B91] rounded-[10px] text-[#fff]">{props.currentpage}</div>
            <button className="font-inter text-[30px] font-medium leading-normal text-[#BEC6CF]" onClick={handleIncrease}>→</button>
          </div>
        </div>
      </div>
      {(props.isAdd || props.isDetailProgress) && (
        <>
          <hr className="bg-[#6ABFFD] mb-[20px] border-solid w-[960px] h-[4px]" />
          <div className="h-[600px] w-[960px]">
            <h5 className="font-sans text-[24px] font-semibold leading-[36px] text-[#032B91]">
              {props.isDetailProgress
                ? `#0000${objProgress.id}`
                : "Tiến trình mới"}
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
                    value={objProgress.date_performance}
                  />
                  <img
                    src="/images/Patient_calender.png"
                    alt=""
                    onClick={toggleDatePicker}
                  />
                  {showDatePicker && (
                    <div style={{ position: "relative" }}>
                      <Datepicker
                        className="absolute top-5 right-0"
                        inline
                        onSelectedDateChanged={handleDateChange}
                      />
                    </div>
                  )}
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
                <input
                  className="w-[450px] h-[48px] py-[12px] px-[8px]  flex items-center self-stretch rounded-[5px]"
                  type="text"
                  placeholder="10:00"
                  value={objProgress.time_performance}
                  onChange={(e) => {
                    setTime_performance(e.target.value);
                    setObjProgress({
                      ...objProgress,
                      start_treatment: `${date_performance} ${e.target.value}:00`,
                      time_performance: `${e.target.value}`,
                    });
                  }}
                />
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
                    value={objProgress.date_finished}
                  />
                  <img
                    src="/images/Patient_calender.png"
                    alt=""
                    onClick={toggleDatePickerFinished}
                  />
                  {showDatePickerFinished && (
                    <div style={{ position: "relative" }}>
                      <Datepicker
                        className="absolute top-5 right-0"
                        inline
                        onSelectedDateChanged={handleDateChangeFinished}
                      />
                    </div>
                  )}
                </div>
              </div>

              <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                  <h6 className="font-sans text-[20px] font-medium leading-[32px]">
                    Giờ kết thúc{" "}
                  </h6>
                </div>

                <input
                  className="w-[450px] h-[48px] py-[12px] px-[8px]  flex items-center self-stretch rounded-[5px]"
                  type="text"
                  placeholder="20:00"
                  value={objProgress.time_finished}
                  onChange={(e) => {
                    setTime_finished(e.target.value);
                    setObjProgress({
                      ...objProgress,
                      end_treatment: `${date_finished} ${e.target.value}:00`,
                      time_finished: `${e.target.value}`,
                    });
                  }}
                />
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
                  value={objProgress.patient_condition}
                  onChange={(e) =>
                    setObjProgress({
                      ...objProgress,
                      patient_condition: e.target.value,
                    })
                  }
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
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] flex items-center self-stretch rounded-[5px]">
                  <select
                    className="block appearance-none w-full text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="grid-state"
                    type="text"
                    placeholder="SCHEDULING"
                    value={objProgress.status}
                    onChange={(e) =>
                      setObjProgress({ ...objProgress, status: e.target.value })
                    }
                  >
                    <option>SCHEDULING</option>
                    <option>PROCESSING</option>
                    <option>FINISHED</option>
                  </select>
                </div>
              </div>

              {props.isDetailProgress && <AddStaff />}

              {props.isDetailProgress &&
                Array.from({ length: props.numStaffAdded }, (_, index) => (
                  <AddStaffNonHeader
                    key={index}
                    removeStaffAdded={props.removeStaffAdded}
                  />
                ))}

              {props.isDetailProgress && (
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
              )}
            </div>
          </div>
        </>
      )}
    </>
  );
}

export default ProgressContent;

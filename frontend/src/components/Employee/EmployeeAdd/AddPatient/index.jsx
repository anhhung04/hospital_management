import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./style.css" 
import FormList from "./FormList";
import ListBar from "../../Component/ListBar/ListBar";
import apiCall from "../../../../utils/api";

function AddPatient({empId}) {
    // const props = {
    //     start_treatment: "2024-05-06 00:00:00",
    //     patient_id: "sdfsdsdsdsds",
    //     patient_name: "Nguyen Quynh Nhu",
    //     status: "Den lich hen"

    // }
    const [patientList, setPatientList] = useState([])
    const [pageNumber, setPageNumber] = useState(1);

    const navigate = useNavigate();
    const handlePatientDetail = (patientId) => {
        navigate(`/patient`);
    };
    useEffect(() => {
        apiCall({
            endpoint: `/api/patient/progress/in-charge?doctor_id=${empId}&limit=${20}`,
            method: "GET"
        })
        .then((data) => {
            console.log("My employee patient list", data)
            if(data && data?.data && data.data?.length > 0){
              setPatientList(data.data);
            }
            else 
              setPatientList([]);
          })
          .catch((error) => console.error('Error fetching employee data:', error));
      }, []);

    return (
        <div className="table-conttainer w-full px-[60px] py-[40px] h-[530px]">            
            <div className="header flex justify-between items-center">
                <div className="left-header flex items-center">
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
            <div className="list-content flex flex-col justify-between items-center w-full mt-[20px]">
                <FormList prop = {["STT", "Bệnh nhân", "Ngày thực hiện", "Giờ thực hiện", "Tình trạng", "Chi tiết"]}/>
                <div className="h-[268px] my-[20px] w-full flex justify-center">
                    {patientList.length === 0  && <p className="text-black text-[34px] not-italic font-medium leading-[48px] mt-[30px]">Chưa có dữ liệu nào</p>}
                    {patientList.length !== 0 && 
                        <div className="w-full flex flex-col gap-[8px]">
                            {patientList.slice((pageNumber - 1)*5, (pageNumber - 1)*5 + 5).map((uniPatient, index) => (
                                <div className="header flex h-[36px] items-center w-full">
                                    <div key={index} className={`header-content flex w-full items-center ${uniPatient?.status === "Den lich hen" ? "bg-[#E8FCEC]" : ""}`}>
                                        <p className="text-black font-normal leading-6 flex justify-center w-[70px]">{index + 1}</p>
                                        <p className="text-black font-normal leading-6 flex justify-center w-[210px]">{uniPatient?.patient_name || "Không có"}</p>
                                        <p className="text-black font-normal leading-6 flex justify-center w-[180px]">{uniPatient?.start_treatment? uniPatient.start_treatment.split(' ')[0] : "Không có"}</p>
                                        <p className="text-black font-normal leading-6 flex justify-center w-[220px]">{uniPatient?.start_treatment? uniPatient.start_treatment.split(' ')[1] : "Không có"}</p>
                                        <p className="text-black font-normal leading-6 flex justify-center w-[140px]">{uniPatient?.status || "Chưa đến lịch"}</p>
                                        <p className="text-[#0544E4] font-normal leading-6 pr-[20px] flex justify-end w-[140px]" onClick={() => handlePatientDetail(uniPatient?.patient_id)}>Hồ sơ ↗</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    }
                     {/* <div className="header flex h-[36px] items-center w-full">
                        <div className={`header-content flex w-full items-center ${props?.status === "Den lich hen" ? "bg-[#E8FCEC]" : ""}`}>
                            <p className="text-black font-normal leading-6 flex justify-center w-[70px]">{1}</p>
                            <p className="text-black font-normal leading-6 flex justify-center w-[210px]">{props?.patient_name || "Không có"}</p>
                            <p className="text-black font-normal leading-6 flex justify-center w-[180px]">{props?.start_treatment? props.start_treatment.split(' ')[0] : "Không có"}</p>
                            <p className="text-black font-normal leading-6 flex justify-center w-[220px]">{props?.start_treatment? props.start_treatment.split(' ')[1] : "Không có"}</p>
                            <p className="text-black font-normal leading-6 flex justify-center w-[140px]">{props?.status || "Chưa đến lịch"}</p>
                            <p className="text-[#0544E4] font-normal leading-6 pr-[20px] flex justify-end w-[140px]" onClick={() => handlePatientDetail(props?.patient_id)}>Hồ sơ ↗</p>
                        </div>
                     </div> */}

                </div>

                <div className="flex justify-between w-full">
                    <div>
                        <p className='text-black text-lg font-medium leading-6'>Tổng số lượng: {patientList.length}</p>
                    </div>
                    <ListBar pageNumber={pageNumber} inForm={true} handlePage={(page) => setPageNumber(page)}/>
                </div>
                </div>
        </div>
    )
}

export default AddPatient;
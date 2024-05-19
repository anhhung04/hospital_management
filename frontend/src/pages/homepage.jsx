import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import apiCall from "../utils/api";
import Chart from "../components/Chart";

const fakePatient =
        [
            {
                "id": "e523fa4e-0adf-4860-89a6-213c15755f29",
                "full_name": "A Nguyen Van",
                "phone_number": "01923019231",
                "appointment_date": null,
                "medical_record_id": 129
            },
            {
                "id": "6017747c-d5b3-48cb-83f1-bb49a6053cc8",
                "full_name": "An Nguyen",
                "phone_number": "981391289312",
                "appointment_date": null,
                "medical_record_id": 196
            },
            {
                "id": "a7830e0d-f60a-431f-970c-d5c62133a717",
                "full_name": "Ly Nguyen Van",
                "phone_number": "731928312093",
                "appointment_date": null,
                "medical_record_id": 199
            },
            {
                "id": "23fac36d-6619-483c-8641-048a30158e4d",
                "full_name": "Chi Nguyen",
                "phone_number": "123091023",
                "appointment_date": null,
                "medical_record_id": 348
            },
            {
                "id": "41bed50c-7d07-444d-9338-71f7a6a47cf0",
                "full_name": "Mai Anh Hoang Thi",
                "phone_number": "091231293129",
                "appointment_date": null,
                "medical_record_id": 352
            }
        ]
    
        const fakeEmployee = [
            {
                "id": "189a8780-98f2-45de-8522-a048b36beb9e",
                "full_name": "Nguyễn Văn L",
                "faculty": "Back Khoa University",
                "status": null,
                "employee_type": "MANAGER",
                "education_level": null,
                "begin_date": "2020-01-01",
                "end_date": "2024-12-01"
            },
            {
                "id": "289a8780-98f2-45de-8522-a048b36beb9e",
                "full_name": "Nguyễn Thị B",
                "faculty": "Back Khoa University",
                "status": null,
                "employee_type": "DOCTOR",
                "education_level": null,
                "begin_date": "2020-01-01",
                "end_date": "2024-12-01"
            },
            {
                "id": "96961e57-12fb-4580-954d-8a5cdf1337d9",
                "full_name": "DSD DSDS",
                "faculty": null,
                "status": null,
                "employee_type": "NURSE",
                "education_level": null,
                "begin_date": "None",
                "end_date": "None"
            },
            {
                "id": "0a841fd6-bb68-43b1-98a0-5fd8b266122e",
                "full_name": "Nguyen Nhu",
                "faculty": null,
                "status": null,
                "employee_type": "NURSE",
                "education_level": null,
                "begin_date": "None",
                "end_date": "None"
            },
            {
                "id": "cfd71154-16ee-4e59-b6aa-8923b9be108a",
                "full_name": "nguyen a",
                "faculty": null,
                "status": null,
                "employee_type": "DOCTOR",
                "education_level": null,
                "begin_date": "None",
                "end_date": "None"
            }
        ]

function Homepage() {

    // const [general_info, setGeneralinfo] = useState([]);
    const [listpatient, setPatients] = useState([]);
    const [listemployee, setEmployees] = useState([]); 
    const [metric, setMetric] = useState({});

    const [isBlur, setIsBlur] = useState("");
    

    const [metricData, setMetricData] = useState([]);

    function handleData(numbers) {
        // console.log("numbers",numbers); 
        const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
        const result = days.map((day, index) => ({
            x: day,
            y: numbers[index]
          }));
        return result;
    }
    
    useEffect(() => {
        apiCall({endpoint: "/api/patient/list?page=1&limit=5"})
            .then((data) => {
                if(data.status_code === 200){
                    setPatients(data.data);
                }else{
                    setPatients(fakePatient);
                    setIsBlur("blur-md");
                }
                
                // console.log(data);
            });
    }, []);

    useEffect(() => {
        apiCall({endpoint: "/api/employee/list?page=1&limit=5"})
            .then((data) => {
                
                if(data.status_code === 200){
                    setEmployees(data.data);
                }else{
                    setEmployees(fakeEmployee);
                    setIsBlur("blur-md");
                }
                // console.log(data);
            })},[]);

    useEffect(() => {
        apiCall({endpoint: "/api/metric/"})
            .then((data) => {
                setMetric(data.data);
                setMetricData(handleData(data.data.patients_per_day));
                // console.log(data);
            })},[]);

    console.log("listpatient1111111",listpatient);
    console.log("listemployee",listemployee);
    console.log("metricData",metricData);

    const navigate = useNavigate();

    //console.log("data",typeof listpatient.data);
 
    return ( <div className={`w-full bg-[#EFF7FE] flex justify-center items-center`}>
        <div className="w-[1080px] h-[1116px] flex flex-col gap-[45px]">
            <div className="w-[1080px] h-[98px] inline-flex flex-between gap-[40px]">
                {/* {.map((info, index) => (
                    <div key={index} className="w-[240px] h-[98px] bg-[#FFFF] rounded-full shadow-2xl gap-[7px] inline-flex flex-start justify-center items-center">
                        <div className="w-[50px] h-[50px] flex justify-center items-center" onClick={()=>navigate(info.path)} ><img src="/images/image 6.png" alt="logo" className="hover:size-[50px]" /></div>
                        <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
                            <h3 className="font-sans text-[18px] font-medium text-left leading-[24px]">{info.value}</h3>
                            <h3>{info.title}</h3>
                        </div>
                    </div>
                ))} */}
                <div className="w-[240px] h-[98px] bg-[#FFFF] rounded-full shadow-2xl gap-[7px] inline-flex flex-start justify-center items-center">
                        <div className="w-[50px] h-[50px] flex justify-center items-center" onClick={()=>navigate("/patient")} ><img src="/images/image 6.png" alt="logo" className="hover:size-[50px]" /></div>
                        <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
                            <h3 className="font-sans text-[18px] font-medium text-left leading-[24px]">{metric.num_patients}</h3>
                            <h3>Bệnh nhân</h3>
                        </div>
                </div>
                <div className="w-[240px] h-[98px] bg-[#FFFF] rounded-full shadow-2xl gap-[7px] inline-flex flex-start justify-center items-center">
                        <div className="w-[50px] h-[50px] flex justify-center items-center" onClick={()=>navigate("/employee")} ><img src="/images/image 6.png" alt="logo" className="hover:size-[50px]" /></div>
                        <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
                            <h3 className="font-sans text-[18px] font-medium text-left leading-[24px]">{metric.num_employee}</h3>
                            <h3>Nhân viên</h3>
                        </div>
                </div>
                <div className="w-[240px] h-[98px] bg-[#FFFF] rounded-full shadow-2xl gap-[7px] inline-flex flex-start justify-center items-center">
                        <div className="w-[50px] h-[50px] flex justify-center items-center" onClick={()=>navigate("/employee")} ><img src="/images/image 6.png" alt="logo" className="hover:size-[50px]" /></div>
                        <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
                            <h3 className="font-sans text-[18px] font-medium text-left leading-[24px]">{metric.num_nurses}</h3>
                            <h3>Y tá</h3>
                        </div>
                </div>

                <div className="w-[240px] h-[98px] bg-[#FFFF] rounded-full shadow-2xl gap-[7px] inline-flex flex-start justify-center items-center">
                        <div className="w-[50px] h-[50px] flex justify-center items-center" onClick={()=>navigate("/employee")} ><img src="/images/image 6.png" alt="logo" className="hover:size-[50px]" /></div>
                        <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
                            <h3 className="font-sans text-[18px] font-medium text-left leading-[24px]">{metric.num_doctors}</h3>
                            <h3>Bác sĩ</h3>
                        </div>
                </div>
            </div>
            <div className="w-[1080] h-[490px] flex flex-start gap-[40px]">
                <div className="w-[644px] h-[490px] bg-[#FFF] rounded-[47px] shadow-xl">
                    <div className="w-[170px] h-[36px] rounded-lg mt-[40px] ml-[40px]">
                        <h5 className="font-sans text-[24px] font-semibold leading-[36px] text-[#032B91] text-left ">Bệnh nhân</h5>
                    </div>
                    <div className="mt-[20px] ml-[25px] w-[594px] h-[56px] bg-[#CDDBFE] rounded-2xl px-[22px] py-[12px] inline-flex items-center justify-center gap-[76px] shadow-md">
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">STT</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Tên</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Giờ</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Chi Tiết</h6>
                    </div>
                    <div className={`w-[594px] h-[280px] mx-[25px] mt-[20px] flex flex-col items-start gap-[12px] ${isBlur}`}>
                        {listpatient?.map((patient, index) => (<div key={index} className="w-[594px] h-[44px] px-[20px] py-[10px] flex items-center gap-[12px] ">
                            <h4 className="font-sans text-[16px] font-normal leading-[24px] w-[55px] text-right">{index}</h4>
                            <h4 className="font-sans text-[16px] font-normal leading-[24px] w-[140px] text-left ml-[5px]">{patient.full_name}</h4>
                            <h4 className="font-sans text-[16px] font-normal leading-[24px] w-[92px] text-left">10:00</h4>
                            <h4 className="font-sans text-[16px] font-normal leading-[24px] w-[92px] text-left">2024-5-12</h4>
                            <h4 className="font-sans  text-[16px] font-normal leading-[24px] w-[109px] text-right text-[#0544E4]">Hồ sơ ↗</h4>
                        </div>))
                            }
                    </div>
                </div>

                <div className="w-[396px] h-[490px] bg-[#FFF] rounded-[47px] shadow-xl">
                    <div className="w-[170px] h-[36px] rounded-lg mt-[40px] ml-[40px]">
                        <h5 className="font-sans text-[24px] font-semibold leading-[36px] text-[#032B91] text-left ">Bác Sĩ</h5>
                    </div>
                    <div className="mt-[20px] ml-[25px] w-[346px] h-[56px] bg-[#CDDBFE] rounded-2xl px-[22px] py-[12px] inline-flex items-center justify-center gap-[48px] shadow-md">
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">STT</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Tên</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Tình trạng</h6>
                    </div>
                    <div className={`w-[346px] h-[280px] mt-[20px] ml-[25px] flex flex-col items-start gap-[12px] ${isBlur}`}>
                        {/* <div className="w-[346px] h-[44px] px-[20px] py-[10px] flex items-center gap-[12px]"> */}
                            {listemployee?.map((employee, index) => (<div key={index} className="w-[346px] h-[44px] px-[20px] py-[10px] flex items-center gap-[12px] ">
                                <h4 className="font-sans text-[16px] font-normal leading-[24px] w-[55px] text-right">{index}</h4>
                                <h4 className="font-sans text-[16px] font-normal leading-[24px] w-[140px] text-left ml-[5px]">{employee.full_name}</h4>
                                <h4 className="font-sans text-[16px] font-normal leading-[24px] w-[92px] text-left text-[#00F40A]" >Trống</h4>
                            </div>
                            ))
                                }
                        {/* </div> */}
                    </div>
                </div>
            </div>
            <div className="w-[1080px] h-[437px] bg-[#FFF] rounded-[47px] shadow-xl">
                    <Chart metricData={metricData}/>
            </div>
        </div>
    </div> );
}

export default Homepage;
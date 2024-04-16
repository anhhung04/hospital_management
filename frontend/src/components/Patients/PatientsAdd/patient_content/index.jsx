import { useState } from "react";
import { Datepicker } from "flowbite-react";
import { useEffect } from "react";
import apiCall from "../../../utils/api";
import PropTypes from 'prop-types';

PatientContent.propTypes = {
    isPatientSubmit: PropTypes.bool,
    setResDataPatient: PropTypes.func,
    handleSubmitFailed: PropTypes.func
};

function PatientContent(props) {
    const [patient_id, setPatient_id] = useState("");
    const [showDatePicker, setShowDatePicker] = useState(false);
    const [signup_date, setSignup_date] = useState("");
    const [height, setHeight] = useState("");
    const [weight, setWeight] = useState("");
    const [current_treatment, setCurrent_treatment] = useState("");
    const [drug_allergies, setDrug_allergies] = useState("");
    const [food_allergies, setFood_allergies] = useState("");
    const [medical_history, setMedical_history] = useState("");
    // console.log("patient",patient_id)
    // console.log("signup",signup_date)
    // console.log("height",height)
    // console.log("weight",weight) 
    // console.log("current_treatment",current_treatment)
    // console.log("drug_allergies",drug_allergies)
    // console.log("food_allergies",food_allergies)
    // console.log("medical_history",medical_history)
      
    function toggleDatePicker() {
        setShowDatePicker(pre => !pre);
    }

    const handleDateChange = (selectedDate) => {
        const month = selectedDate.getMonth() + 1; // Months are zero-based, so add 1
        const day = selectedDate.getDate();
        const year = selectedDate.getFullYear();
        setSignup_date(`${year}-${month}-${day}`);
        setShowDatePicker(false);
    };

    function handlecurrent_treatment(e){
        setCurrent_treatment(e.target.value)
    }

    function handledrug_allergies(e){
        setDrug_allergies(e.target.value)
    }

    function handlefood_allergies(e){   
        setFood_allergies(e.target.value) 
    }

    function handlemedical_history(e){
        setMedical_history(e.target.value)
    }

    function checkInfoItem() {
        if (patient_id === "" || signup_date === "" || height === "" || weight === "") {
            props.handleSubmitFailed();
        }
    }

    

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
      }
    const api_patient_id = getCookie('user_id');
    //console.log("api_patient_id",api_patient_id)

    useEffect(() => {
        if (props.isPatientSubmit) {
            checkInfoItem();
            // console.log("api_patient_id",api_patient_id)
            const data = {
                "medical_record": {
                    "weight": weight,
                    "height": height,
                    "note": "",
                    "current_treatment": current_treatment,
                    "drug_allergies": drug_allergies,
                    "food_allergies": food_allergies,
                    "medical_history": medical_history
                  }
            };
            console.log("my api patient:",`/api/patient/${api_patient_id}/update`)
            apiCall({
                endpoint: `/api/patient/${api_patient_id}/update`,
                method: "PATCH",
                requestData: data,
            }).then((res_data) => {
                console.log(res_data);
                props.setResDataPatient(res_data);
            });
        }
    }, [props.isPatientSubmit]);

    return ( <div className="w-[1080px] h-[836px] px-[60px] py-[40px] flex flex-col gap-[40px] items-start">
        <div className=" h-[208px] w-full grid grid-cols-2 gap-x-[60px] gap-y-[40px] content-start">
            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Mã bệnh nhân <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input 
                    className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]"
                    type="text" 
                    placeholder="#0000001" 
                    value={patient_id}
                    onChange={(e) => setPatient_id(e.target.value)}
                />

            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày đăng ký hồ sơ <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                <input 
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" 
                    type="text" 
                    placeholder="10/03/2024" 
                    value={signup_date} 
                    onChange={(e) => setSignup_date(e.target.value)}
                />

                    <img src="/images/Patient_calender.png" alt="" onClick={toggleDatePicker}/>
                    {showDatePicker && (
                            <div style={{ position: "relative" }}>
                                <Datepicker className="absolute top-5 right-0" inline onSelectedDateChanged={handleDateChange} />
                            </div>
                        )}
                </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Chiều cao <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                <input 
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" 
                    type="text" 
                    placeholder="170" 
                    value={height} 
                    onChange={(e) => setHeight(e.target.value)}
                />
                    <div className="w-[24px] h-[24px] flex justify-center items-center ">
                        <h3 className="font-sans text-[14px] font-medium leading-[24px] text-[#6E7F94] ">cm</h3>
                    </div>
                </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Cân nặng <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                <input 
                    className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" 
                    type="text" 
                    placeholder="55" 
                    value={weight} 
                    onChange={(e) => setWeight(e.target.value)}
                />
                    <div className="w-[24px] h-[24px] flex justify-center items-center ">
                        <h3 className="font-sans text-[14px] font-medium leading-[24px] text-[#6E7F94] ">kg</h3>
                    </div>
                </div>
            </div>
        </div>
        <div className="w-[960px] h-[280px] flex flex-row gap-[34px] justify-start self-stretch content-start ">
            <div className="w-[360px] h-[228px] flex flex-col gap-[20px] ">
                <h6 className="font-sans text-[20px] font-medium leading-[32px] ">Vui lòng điền thông tin sức khỏe sau</h6>
                <div className="flex flex-col items-start gap-[12px]">
                    <div className="px-[8px] py-[12px] rounded-[5px] flex items-center">
                        <h6 className="font-sans text-[16px] font-medium leading-[24px]">Hiện tại bạn có đang điều trị gì không?</h6>
                    </div>
                    <div className="px-[8px] py-[12px] rounded-[5px] flex items-center">
                        <h6 className="font-sans text-[16px] font-medium leading-[24px]">Bạn có bị dị ứng thực phẩm gì không?</h6>
                    </div>
                    <div className="px-[8px] py-[12px] rounded-[5px] flex items-center">
                        <h6 className="font-sans text-[16px] font-medium leading-[24px]">Bạn có bị ứng thuốc không?</h6>
                    </div>
                    <div className="px-[8px] py-[12px] rounded-[5px] flex items-center">
                        <h6 className="font-sans text-[16px] font-medium leading-[24px]">Bạn có tiền sử bệnh án gì không?</h6>
                    </div>
                </div>
            </div>
            <div className="w-[156px] h-[268px] flex flex-col gap-[32px]">
                <div className="w-[156px] h-[32px] flex flex-row items-center">
                    <h6 className="text-[20px] text-center font-sans font-medium leading-[32px] mr-[25px]">Có</h6>
                    <h6 className="text-[20px] text-center font-sans font-medium leading-[32px] mr-[24px]">Không</h6>
                    <h6 className="text-[20px] text-center font-sans font-medium leading-[32px] mr-[30px]">NA</h6>
                </div>
                <div className="w-[156px] h-[199px] gap-[45px] flex flex-col items-center">
                    <div className="flex items-start gap-[54px]">
                        <input type="radio" name="option" value="Có" onChange={handlecurrent_treatment} />
                        <input type="radio" name="option" value="Không" onChange={handlecurrent_treatment}/>
                        <input type="radio" name="option" value="NA" onChange={handlecurrent_treatment}/>
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="radio" name="option1" value="Có" onChange={handlefood_allergies} />
                        <input type="radio" name="option1" value="Không" onChange={handlefood_allergies}/>
                        <input type="radio" name="option1" value="NA" onChange={handlefood_allergies}/>
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="radio" name="option2" value="Có" onChange={handledrug_allergies}/>
                        <input type="radio" name="option2" value="Không" onChange={handledrug_allergies}/>
                        <input type="radio" name="option2" value="NA" onChange={handledrug_allergies}/>
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="radio" name="option3" value="Có" onChange={handlemedical_history}/>
                        <input type="radio" name="option3" value="Không" onChange={handlemedical_history}/>
                        <input type="radio" name="option3" value="NA" onChange={handlemedical_history}/>
                    </div>
                </div>
            </div>
            <div className="w-[374px] h-[228px] flex flex-col gap-[20px]">
                <h6 className="font-sans text-[20px] font-medium leading-[32px] ">Nội dung</h6>
                <div className="inline-flex flex-col items-start gap-[12px]">
                    <input className="w-[374px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Nếu có ghi rõ thông tin"/>
                    <input className="w-[374px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Nếu có ghi rõ thông tin"/>
                    <input className="w-[374px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Nếu có ghi rõ thông tin"/>
                    <input className="w-[374px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Nếu có ghi rõ thông tin"/>
                </div>
            </div>
        </div>
        <div className="w-[960px] h-[199px] flex flex-col items-start gap-[4px] shrink-0">
            <div className="w-[960px] h-[32px] flex items-center gap-[4px] self-stretch">
                <h6 className="font-sans text-[20px] font-medium leading-[32px]">Lưu ý khác</h6>
            </div>
            <div className="h-[167px] w-full  flex items-center gap-[8px] shrink-0 self-stretch rounded-[5px] border-[1px] border-solid border-black">
                <input type="text" className=" inline-block align-text-top self-stretch h-full w-full border-0  leading-normal rounded-[5px]" placeholder=""></input>
            </div>
        </div>
    </div> );
}

export default PatientContent;
import { useState } from "react";
import { useEffect } from "react";
import apiCall from "../../../utils/api";
import PropTypes from 'prop-types';

PatientContent.propTypes = {
    isPatientSubmit: PropTypes.bool,
    setResDataPatient: PropTypes.func,
    handleSubmitFailed: PropTypes.func,
    medical_record: PropTypes.object,
    api_patient_id: PropTypes.string,
    setApi_patient_id: PropTypes.func

};

function PatientContent(props) {
    const [patientObj, setPatientObj] = useState({});
    const [api_patient_id, setApi_patient_id] = useState("")
 

    useEffect(() => {
        if(props.medical_record){
            setPatientObj(props.medical_record)
            setApi_patient_id(props.api_patient_id)
        }
    }, [props.medical_record, props.api_patient_id]);
    // console.log("patientObj",patientObj)
    // console.log("props.medical_record",props.medical_record)


    function handlecurrent_treatment(e){
        setPatientObj({...patientObj, current_treatment: e.target.value})
    }

    function handledrug_allergies(e){
        setPatientObj({...patientObj, drug_allergies: e.target.value})
    }

    function handlefood_allergies(e){   
        setPatientObj({...patientObj, food_allergies: e.target.value}) 
    }

    function handlemedical_history(e){
        setPatientObj({...patientObj, medical_history: e.target.value})
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
      }
    //const api_patient_id = getCookie('user_id');
    //console.log("api_patient_id",api_patient_id)
    useEffect(() => {
        if(!props.api_patient_id){
          // const api_patient_id = getCookie('user_id');
          setApi_patient_id(getCookie('user_id'));
        }
      }, [props.api_patient_id]);

    useEffect(() => {
        if (props.isPatientSubmit) {
            // console.log("my api patient:",`/api/patient/${api_patient_id}/update`)
            // console.log("my api patient:",patientObj)   
            apiCall({
                endpoint: `/api/patient/${api_patient_id}/update`,
                method: "PATCH",
                requestData: {"medical_record":patientObj},
            }).then((res_data) => {
                // console.log(res_data);
                props.setResDataPatient(res_data);
            });
        }
    }, [props, api_patient_id,patientObj]);

    return ( <div className="w-[1080px] h-[836px] px-[60px] py-[40px] flex flex-col gap-[40px] items-start">
        <div className=" h-[208px] w-full grid grid-cols-2 gap-x-[60px] gap-y-[40px] content-start">
            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Mã bệnh nhân <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input 
                    className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px] bg-gray-50"
                    type="text" 
                    placeholder="#0000001" 
                    value={api_patient_id}
                    disabled={true}
                />

            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Mã hồ sơ <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                
                <input 
                    className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px] bg-gray-50"
                    type="text" 
                    placeholder="#0000001" 
                    value={patientObj.id} 
                    disabled={true}
                />
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
                    value={patientObj.height} 
                    onChange={(e) => setPatientObj({...patientObj, height: e.target.value})}
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
                    value={patientObj.weight} 
                    onChange={(e) => setPatientObj({...patientObj, weight: e.target.value})}
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
                        <input type="radio" name="option" value="Có" checked={patientObj.current_treatment === "Có"} onChange={handlecurrent_treatment} />
                        <input type="radio" name="option" value="Không" checked={patientObj.current_treatment === "Không"} onChange={handlecurrent_treatment}/>
                        <input type="radio" name="option" value="NA" checked={patientObj.current_treatment === "NA"} onChange={handlecurrent_treatment}/>
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="radio" name="option1" value="Có" checked={patientObj.food_allergies === "Có"} onChange={handlefood_allergies} />
                        <input type="radio" name="option1" value="Không" checked={patientObj.food_allergies === "Không"} onChange={handlefood_allergies}/>
                        <input type="radio" name="option1" value="NA" checked={patientObj.food_allergies === "NA"} onChange={handlefood_allergies}/>
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="radio" name="option2" value="Có" checked={patientObj.drug_allergies === "Có"} onChange={handledrug_allergies}/>
                        <input type="radio" name="option2" value="Không" checked={patientObj.drug_allergies === "Không"} onChange={handledrug_allergies}/>
                        <input type="radio" name="option2" value="NA" checked={patientObj.drug_allergies === "NA"} onChange={handledrug_allergies}/>
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="radio" name="option3" value="Có" checked={patientObj.medical_history === "Có"} onChange={handlemedical_history}/>
                        <input type="radio" name="option3" value="Không" checked={patientObj.medical_history === "Không"} onChange={handlemedical_history}/>
                        <input type="radio" name="option3" value="NA" checked={patientObj.medical_history === "NA"} onChange={handlemedical_history}/>
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
                <input type="text" className=" inline-block align-text-top self-stretch h-full w-full border-0  leading-normal rounded-[5px]" placeholder="" onChange={(e) => setPatientObj({...patientObj, note: e.target.value})} ></input>
            </div>
        </div>
    </div> );
}

export default PatientContent;
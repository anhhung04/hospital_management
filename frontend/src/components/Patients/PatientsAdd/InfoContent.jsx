import { useState, useEffect } from "react";
import apiCall from "../../../utils/api";
import { Datepicker } from "flowbite-react";
import PropTypes from 'prop-types';


InfoContent.propTypes = {
    isSubmit: PropTypes.bool,
    setResDataInfo: PropTypes.func,
    handleSubmitFailed: PropTypes.func
};



function InfoContent(props) {
    const [first_name, setFirst_name] = useState("");
    const [last_name, setLast_name] = useState("");
    const [birth_date, setBirth_date] = useState("");
    const [gender, setGender] = useState("");
    const [id_card, setId_card] = useState("");
    const [phone, setPhone] = useState("");
    const [address, setAddress] = useState("");
    const [email, setEmail] = useState("");
    const [health_insurance, setHealth_insurance] = useState("");
    const [showDatePicker, setShowDatePicker] = useState(false);


    function toggleDatePicker() {
        setShowDatePicker(pre => !pre);
    }

    const handleDateChange = (selectedDate) => {
        const month = selectedDate.getMonth() + 1; // Months are zero-based, so add 1
        const day = selectedDate.getDate();
        const year = selectedDate.getFullYear();
        setBirth_date(`${year}-${month}-${day}`);
        setShowDatePicker(false);
    };


     const checkInfoItem = () =>{
        if (first_name === "" || last_name === "" || birth_date === "" || gender==="" || id_card==="" || phone==="" || address==="") {
            props.handleSubmitFailed
        }
    }


    useEffect(() => {
        if (props.isSubmit) {
            checkInfoItem();
            const data = {
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date,
                "gender": gender,
                "ssn": id_card,
                "phone_number": phone,
                "address": address,
                "email": email,
                "health_insurance": health_insurance
            };
            
            apiCall({
                endpoint: "/api/patient/create",
                method: "POST",
                requestData: data,
            }).then((res_data) => {
                console.log(res_data);
                props.setResDataInfo(res_data);
            });
        }
    }, [props.isSubmit, first_name, last_name, birth_date, gender, id_card, phone, address, email, health_insurance]);
    
        

    return ( <div className="w-[1080px] h-[836px] px-[60px] py-[40px] flex justify-center items-center">
        <div className=" h-full w-full grid grid-cols-2 gap-x-[60px] gap-y-[40px] content-start">
            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Họ <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" 
                type="text" placeholder="Nguyễn" onChange={(e)=>setFirst_name(e.target.value)}/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Tên <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]"
                 type="text" placeholder="Văn A" onChange={(e)=>setLast_name(e.target.value)}/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày sinh <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]"
                     type="text" placeholder="10/03/2024" value={birth_date} onChange={(e)=>setBirth_date(e.target.value)}/>
                    <img src="/images/Patient_calender.png" alt="" onClick={toggleDatePicker} />
                    {showDatePicker && (
                            <div style={{ position: "relative" }}>
                                <Datepicker className="absolute top-5 right-0" inline onSelectedDateChanged={handleDateChange} />
                            </div>
                        )}
                </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Giới tính <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    {/* <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]"
                     type="text" placeholder="Nam" onChange={(e)=>setGender(e.target.value)}/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" /> */}
                    <select className="block appearance-none w-full border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-state"
                    type="text" placeholder="Nam" onChange={(e)=>setGender(e.target.value)}>
                        <option>Nam</option>
                        <option>Nữ</option>
                        <option>Khác</option>
                    </select>
                </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">CCCD <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]"
                 type="text" placeholder="0123456789" onChange={(e)=>setId_card(e.target.value)}/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Số điện thoại <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-solid border-black flex items-center self-stretch rounded-[5px]"
                 type="text" placeholder="0903812312" onChange={(e)=>setPhone(e.target.value)}/>
            </div>

            <div className="w-[960px] h-[84px] col-span-2">
            <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Địa chỉ <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[960px] h-[48px] col-span-2">
                <input type="text" className="w-[960px] h-[48px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]"
                 placeholder="268 Lý Thường Kiệt, Phường 14, Quận 10, Thành phố Hồ Chí Minh, Việt Nam" onChange={(e)=>setAddress(e.target.value)}/>
            </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Email</h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]"
                 type="text" placeholder="nguyenvana@gmail.com" onChange={(e)=>setEmail(e.target.value)}/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Thẻ bảo hiểm y tế</h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-solid border-black flex items-center self-stretch rounded-[5px]"
                 type="text" placeholder="HS0123456789" onChange={(e)=>setHealth_insurance(e.target.value)}/>
            </div>
        </div>
    </div> );
}



export default InfoContent;
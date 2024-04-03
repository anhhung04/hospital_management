import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";


function Homepage() {

    const [general_info, setGeneralinfo] = useState([]);

    useEffect(() => {
        fetch("/api/generalinfo")
            .then((response) => response.json())
            .then((data) => {
                setGeneralinfo(data);
                // console.log(data);
            });
    }, []);  

    const navigate = useNavigate();
 
    return ( <div className="w-full bg-[#EFF7FE] flex justify-center items-center">
        <div className="w-[1080px] h-[1116px] flex flex-col gap-[45px]">
            <div className="w-[1080px] h-[98px] inline-flex flex-between gap-[40px]">
                {general_info.map((info, index) => (
                    <div key={index} className="w-[240px] h-[98px] bg-[#FFFF] rounded-full shadow-2xl gap-[7px] inline-flex flex-start justify-center items-center">
                        <div className="w-[50px] h-[50px] flex justify-center items-center" onClick={()=>navigate(info.path)} ><img src="/images/image 6.png" alt="logo" className="hover:size-[50px]" /></div>
                        <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
                            <h3 className="font-sans text-[18px] font-medium text-left leading-[24px]">{info.value}</h3>
                            <h3>{info.title}</h3>
                        </div>
                    </div>
                ))}
            </div>
            <div className="w-[1080] h-[490px] flex flex-start gap-[40px]">
                <div className="w-[644px] h-[490px] bg-[#FFF] rounded-[47px] shadow-xl">
                    <div className="w-[170px] h-[36px] rounded-lg mt-[40px] ml-[40px]">
                        <h5 className="font-sans text-[24px] font-semibold leading-[36px] text-[#032B91] text-left ">Bệnh nhân</h5>
                    </div>
                    <div className="mt-[20px] ml-[25px] w-[594px] h-[56px] bg-[#CDDBFE] rounded-2xl px-[22px] py-[12px] inline-flex items-center justify-center gap-[48px] shadow-md">
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">STT</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Tên</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Giờ</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Bác Sĩ</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Chi Tiết</h6>
                    </div>
                </div>

                <div className="w-[396px] h-[490px] bg-[#FFF] rounded-[47px] shadow-xl">
                    <div className="w-[170px] h-[36px] rounded-lg mt-[40px] ml-[40px]">
                        <h5 className="font-sans text-[24px] font-semibold leading-[36px] text-[#032B91] text-left ">Bác Sĩ</h5>
                    </div>
                    <div className="mt-[20px] ml-[25px] w-[346px] h-[56px] bg-[#CDDBFE] rounded-2xl px-[22px] py-[12px] inline-flex items-center justify-center gap-[48px] shadow-md">
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">STT</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Tên</h6>
                        <h6 className="font-sans text-[20px] font-medium leading-[32px]">Giờ</h6>
                    </div>
                </div>
            </div>
            <div className="w-[1080px] h-[437px] bg-[#FFF] rounded-[47px] shadow-xl"></div>
        </div>
    </div> );
}

export default Homepage;
import HuyButton from "../../../../Button/Huy_Button";
import LuuButton from "../../../../Button/Luu_Button";
import { useState } from "react";


function AddResult(props) {
    const [typeCheck, setTypeCheck] = useState("");
    const [result, setResult] = useState("");
    const [date, setDate] = useState("");
    const [time, setTime] = useState("");
    const [dateResult, setDateResult] = useState("");
    const [timeResult, setTimeResult] = useState("");


    console.log(typeCheck);
    console.log(result);
    console.log(date);
    console.log(time);
    console.log(dateResult);
    console.log(timeResult);
  return (
    <div className="fixed inset-0 bg-black bg-opacity-30 backdrop-blur-sm flex justify-center items-center">
      <div className="bg-white w-[769px] h-[484px] flex flex-col  ml-[11%] p-[24px] gap-[24px] rounded-[32px] ">
        <div className="w-[721px] h-[36px] flex items-center gap-[8px] self-stretch justify-between ">
          <h5 className="font-sans text-[24px] font-semibold leading-[36px]">
            Thêm kết quả kiểm tra mới
          </h5>
          <img src="/images/Alert_exit_button.png" alt="Exit Button" onClick={props.setAddResult}/>
        </div>
        <div className="h-[300px] w-full grid grid-cols-2 items-start  gap-x-[41px]">
            <div className="w-[340px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[340px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Loại kiểm tra <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[340px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024" onChange={(e)=>setTypeCheck(e.target.value)}/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
            </div>

            <div className="w-[340px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[340px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Kết quả </h6>
                </div>
                <div className="w-[340px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024" onChange={(e)=>setResult(e.target.value)} />
                </div>
            </div>

            <div className="w-[340px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[340px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày thực hiện <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[340px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024" onChange={(e)=>setDate(e.target.value)}/>
                    <img src="/images/Patient_calender.png" alt="" />
                </div>
            </div>

            <div className="w-[340px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[340px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Giờ thực hiện <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[340px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024" onChange={(e)=>setTime(e.target.value)}/>
                    <img src="/images/Patient_Trailing_icon.png" alt=""/>
                </div>
            </div>

            <div className="w-[340px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[340px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày có kết quả</h6>
                </div>
                <div className="w-[340px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024" onChange={(e)=>setDateResult(e.target.value)}/>
                    <img src="/images/Patient_calender.png" alt="" />
                </div>
            </div>

            <div className="w-[340px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[340px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Giờ có kết quả</h6>
                </div>
                <div className="w-[340px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024" onChange={(e)=>setTimeResult(e.target.value)}/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
            </div>
        </div>
        <div className="h-[52px] w-full flex flex-row justify-end items-center gap-[18px]">
            <div onClick={props.setAddResult}><HuyButton /></div>
            <div onClick={props.setSuccess}><LuuButton /></div>
            
        </div>
      </div>
    </div>
  );
}

export default AddResult;

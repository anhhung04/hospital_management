function InfoContent() {
    return ( <div className="w-[1080px] h-[836px] px-[60px] py-[40px] flex justify-center items-center">
        <div className=" h-full w-full grid grid-cols-2 gap-x-[60px] gap-y-[40px] content-start">
            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Họ <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Nguyễn"/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Tên <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Văn A"/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày sinh <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024"/>
                    <img src="/images/Patient_calender.png" alt="" />
                </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Giới tính <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="Nam"/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">CCCD <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="0123456789"/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Số điện thoại <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-solid border-black flex items-center self-stretch rounded-[5px]" type="text" placeholder="0903812312"/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Địa chỉ <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-black border-[1px] border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="Quốc gia"/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
            </div>

            <div className="w-[450px] h-[48px] pt-[36px] flex items-end gap-[4px]">
            <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-black border-[1px] border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="Quốc gia"/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
            </div>
            <div className="w-[450px] h-[48px] flex items-end gap-[4px]">
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-black border-[1px] border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="Quốc gia"/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
            </div>
            <div className="w-[450px] h-[48px] flex items-end gap-[4px]">
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-black border-[1px] border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="Quốc gia"/>
                    <img src="/images/Patient_Trailing_icon.png" alt="" />
                </div>
            </div>
            <div className="w-[960px] h-[48px] col-span-2">
                <input type="text" className="w-[960px] h-[48px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" placeholder="Số nhà" />
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Email <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Quốc gia"/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Thẻ bảo hiểm y tế <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-solid border-black flex items-center self-stretch rounded-[5px]" type="text" placeholder="Quốc gia"/>
            </div>
        </div>
    </div> );
}

export default InfoContent;
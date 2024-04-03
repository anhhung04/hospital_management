function PatientContent() {
    return ( <div className="w-[1080px] h-[836px] px-[60px] py-[40px] flex flex-col gap-[40px] items-start">
        <div className=" h-[208px] w-full grid grid-cols-2 gap-x-[60px] gap-y-[40px] content-start">
            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Mã bệnh nhân <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <input className="w-[450px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="#0000001"/>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Ngày đăng ký hồ sơ <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="10/03/2024"/>
                    <img src="/images/Patient_calender.png" alt="" />
                </div>
            </div>

            <div className="w-[450px] h-[84px] flex flex-col items-start gap-[4px]">
                <div className="w-[450px] h-[32px] flex items-center gap-[4px] self-stretch">
                    <h6 className="font-sans text-[20px] font-medium leading-[32px]">Chiều cao <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
                </div>
                <div className="w-[450px] gap-[8px] h-[48px] py-[12px] px-[8px] flex items-center self-stretch rounded-[5px] border-[1px] border-black border-solid">
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="170"/>
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
                    <input className="w-[402px] h-[24px] py-[12px] px-[8px] border-0  flex items-center self-stretch rounded-[5px]" type="text" placeholder="55"/>
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
                        <input type="checkbox" />
                        <input type="checkbox" />
                        <input type="checkbox" />
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="checkbox" />
                        <input type="checkbox" />
                        <input type="checkbox" />
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="checkbox" />
                        <input type="checkbox" />
                        <input type="checkbox" />
                    </div>
                    <div className="flex items-start gap-[54px]">
                        <input type="checkbox" />
                        <input type="checkbox" />
                        <input type="checkbox" />
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
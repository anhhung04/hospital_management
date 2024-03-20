
function Login() {
    return ( <div class="w-full h-[1024px] bg-[#EFF7FE] flex justify-center items-center ">
        <div class="bg-[#FFFF] flex flex-col justify-center gap-[4px] rounded-[30px] shadow-2xl w-[613px] h-[568px] p-[40px] ">
            <div class="flex justify-center items-center gap-[10px] p-[10px] self-stretch mb-[24px]">
                <h3 class="font-sans text-[48px] font-medium leading-[72px]"> Đăng Nhập</h3>
            </div>
            <div class="flex items-center mt-0 self-stretch">
                <h6 class="font-sans text-[20px] font-medium leading-[32px]">Tên đăng nhập</h6>
                <h6 class="inline-block text-[#f00] font-sans text-[20px] font-medium leading-[32px]">*</h6>
            </div>
            <input type="text" class="flex py-[12px] px-[8px] self-stretch rounded-[5px] border-solid border-[1px] mb-[20px]" placeholder="Nguyễn Văn A"/>
            <div class="flex flex-col items-start">
                <div class="flex items-center gap-[4px] self-stretch">
                    <h6 class="font-sans text-[20px] font-medium leading-[32px] text-[#000]">Mật khẩu</h6>
                    <h6 class="inline-block text-[#f00] font-sans text-[20px] font-medium leading-[32px]">*</h6>
                </div>
                <input type="text" class="flex py-[12px] px-[8px] gap-[8px] self-stretch rounded-[5px] border-solid border-[1px] mt-[4px] mb-[20px]" placeholder="************"/>
                <div class="flex flex-row items-end w-[200px] h-[16px]">
                    <input type="checkbox" class="bg-[#DBEEFC] mr-[5px]" />
                    <h6 class="font-sans text-[13px] font-medium align-text-bottom text-[#000]">Ghi nhớ tài khoản</h6>
                </div>
                <div class="flex flex-col items-center self-stretch mt-6">
                    <div class="flex p-[10px] flex-col justify-center items-center gap-[10px] self-stretch">  
                        <button class="flex w-[200px] h-[52px] justify-center items-center gap-[10px] rounded-2xl bg-[#032B91] font-sans text-[24px] font-semibold leading-[36px] text-center text-[#F9FBFF]">
                            Đăng nhập
                        </button>
                    </div>
                    <div class="flex justify-center items-center p-[10px] gap-[10px] self-stretch ">
                        <span class="font-sans text-[20px] leading-[32px] font-medium text-[#000]">Quên </span>
                        <span class="font-sans text-[20px] leading-[32px] font-medium text-[#0544E4] hover:text-[#6E7F94]">Tên đăng nhập | mật khẩu</span>
                    </div>
                </div>
            </div>
        </div>
    </div>);
}

export default Login;
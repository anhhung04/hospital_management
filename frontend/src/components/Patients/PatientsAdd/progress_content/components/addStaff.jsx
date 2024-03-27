function AddStaff() {
    return ( <div className="w-full h-[84px] inline-flex items-end content-end gap-[10px] col-span-2 ">
    <div className="w-[294px] h-[84px] flex flex-col items-start gap-[4px]">
        <div className="w-[294px] h-[32px] flex items-center gap-[4px] self-stretch">
            <h6 className="font-sans text-[20px] font-medium leading-[32px]">Nhân viên phụ trách <span className="text-[#F00] text-[20px] font-medium leading-8">*</span></h6>
        </div>
        <input className="w-[294px] h-[48px] py-[12px] px-[8px] border-[1px] border-black border-solid flex items-center self-stretch rounded-[5px]" type="text" placeholder="Mã số nhân viên"/>
    </div>
    <input className="w-[294px] h-[48px] self-end border-[1px] border-black border-solid flex items-center rounded-[5px]" type="text" placeholder="Họ và tên"/>
    <input className="w-[294px] h-[48px] self-end border-[1px] border-black border-solid flex items-center rounded-[5px]" type="text" placeholder="Hàng động"/>
    <div className="w-[48px] h-[48px] bg-[#EFF7FE] border-[1px] border-solid flex items-center justify-center rounded-md">
        <img src="/images/Patient_Garbage.png" alt="Garbage" />
    </div>
</div> );
}

export default AddStaff;
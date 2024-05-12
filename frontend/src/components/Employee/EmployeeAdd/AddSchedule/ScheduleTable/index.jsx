import Scheduler from "./Scheduler";

function ScheduleTable({handleOpenNoti}) {
    return (
        <div>
            <div className="header flex items-center">
                <button className="w-[126px] h-[56px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] rounded-[10px] p-[16px] text-[#032B91] text-xl font-medium leading-8">Hôm nay</button>
                <div className="btn prev px-[36px]">
                    <p className="text-[#032B91] text-2xl font-semibold leading-9">{'<'}</p>
                </div>
                <div className="btn next">
                    <p className="text-[#032B91] text-2xl font-semibold leading-9">{'>'}</p>
                </div>
                <div className="content pl-[36px] text-[#032B91] text-2xl font-semibold leading-9">Tháng 5, 2024</div>
                
            </div>
            <div className="table-container mt-[16px] mb-[38px] w-[958px] h-[502px] rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] flex flex-col justify-center items-center">
                <div className="date w-[958px]">
                    <div className="px-[76px] pt-[20px] header flex justify-between">
                        <p className="text-[#032B91] text-2xl font-semibold leading-9">T2</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9">T3</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9">T4</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9">T5</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9">T6</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9">T7</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9">CN</p>
                    </div>
                    <div className="px-[77px] w-[958px] header flex justify-between">
                        {Array.from({ length: 7 }, (_, index) => (
                            <div className="flex justify-center">
                                <p className="text-[#032B91] text-2xl font-semibold leading-9">{index+19}</p>
                            </div>
                        ))}
                    </div>
                </div>
                <div className="schedule w-[958px]">
                    <Scheduler handleOpenNoti = {handleOpenNoti}/>
                </div>

            </div>
        </div>
    )
}

export default ScheduleTable;

import { useState } from "react";
import Calendar from "./Calendar";
import ScheduleTable from "./ScheduleTable";

function AddSchedule({handleOpenNoti}) {

    return (
        <div>
            <div className="my-[40px] mx-[60px] flex justify-between">
                <Calendar/>
                <div className="info-section flex flex-col pt-[6px]">
                    <div>
                        <p className="text-black text-xl font-medium leading-8">Trạng thái</p>
                        <div className="flex items-center px-[8px] w-[586px] h-[42px] mt-[4px] text-[#9AA6B4] font-medium leading-6 border rounded-[5px] border-solid border-[#9AA6B4]">Ngoài giờ làm</div>
                    </div>
                    <div className="mt-[36px]">
                        <p className="text-black text-xl font-medium leading-8">Ca làm hiện tại</p>
                        <div className="flex items-center px-[8px] w-[586px] h-[42px] mt-[4px] text-[#9AA6B4] font-medium leading-6 border rounded-[5px] border-solid border-[#9AA6B4]">Không có</div>
                    </div>
                </div>
            </div>
            <div className="mx-[60px]">
                <ScheduleTable handleOpenNoti={handleOpenNoti}/>
            </div>
        </div>

    )
}

export default AddSchedule;

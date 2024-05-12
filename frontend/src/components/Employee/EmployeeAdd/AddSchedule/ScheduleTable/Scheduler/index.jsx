import { useState } from "react"
import TimeBox from "../TimeBox";
function Scheduler({handleOpenNoti}) {
    const initialDay = [0, 0, 0, 0, 0, 0, 0];
    const [mon, setMon] = useState(initialDay[0]);
    const [tue, setTue] = useState(initialDay[1]);
    const [wed, setWed] = useState(initialDay[2]);
    const [thu, setThu] = useState(initialDay[3]);
    const [fri, setFri] = useState(initialDay[4]);
    const [sat, setSat] = useState(initialDay[5]);
    const [sun, setSun] = useState(initialDay[6]);
    const colorHover =["hover:bg-[#B3D8F5]", "hover:bg-[#B3F5C1]", "hover:bg-[#FDFFB6]", "hover:bg-[#F9C68A]", "hover:bg-[#FA9189]"];
    const colorFocus =["bg-[#D6F6FF]", "bg-[#E1FBE6]", "bg-[#FEFFDB]", "bg-[#FCE2C5]", "bg-[#FCC8C4]"];
    const handleDay = (day) => {
        if (day === "mon" && mon < 5) setMon(mon + 1);
        else if (day === "tue" && tue < 5) setTue(tue + 1);
        else if (day === "wed" && wed < 5) setWed(wed + 1);
        else if (day === "thu" && thu < 5) setThu(thu + 1);
        else if (day === "fri" && fri < 5) setFri(fri + 1);
        else if (day === "sat" && sat < 5) setSat(sat + 1);
        else if (day === "sun" && sun < 5) setSun(sun + 1);
    }

    return (
        <div className="flex justify-center w-full">
            <div className="mon h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                <div className="h-[386px] mr-[4px] flex flex-col items-center">
                    {Array.from({ length: mon }, (_, index) => (
                        <TimeBox inTime = "10:00 AM" outTime= "9:00 PM" index={index} />
                    ))}
                    {
                        (mon < 5) && 
                        <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[mon]} ${colorHover[mon]}`} onClick={handleOpenNoti}>
                            <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                        </div>
                    }
                </div>
            </div>
            <div className="tue h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                <div className="h-[386px] mx-[4px] flex flex-col items-center">
                    {Array.from({ length: tue }, (_, index) => (
                        <TimeBox inTime = "10:00 AM" outTime= "9:00 PM" index={index} />
                    ))}
                    {
                        (tue < 5) && 
                        <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[tue]} ${colorHover[tue]}`} onClick={handleOpenNoti}>
                            <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                        </div>
                    }
                </div>
            </div>
            <div className="wed h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                <div className="h-[386px] mx-[4px] flex flex-col items-center">
                    {Array.from({ length: wed }, (_, index) => (
                        <TimeBox inTime = "10:00 AM" outTime= "9:00 PM" index={index} />
                    ))}
                    {
                        (wed < 5) && 
                        <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[wed]} ${colorHover[wed]}`} onClick={handleOpenNoti}>
                            <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                        </div>
                    }
                </div>
            </div>
            <div className="thu h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                <div className="h-[386px] mx-[4px] flex flex-col items-center">
                    {Array.from({ length: thu }, (_, index) => (
                        <TimeBox inTime = "10:00 AM" outTime= "9:00 PM" index={index} />
                    ))}
                    {
                        (thu < 5) && 
                        <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[thu]} ${colorHover[thu]}`} onClick={handleOpenNoti}>
                            <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                        </div>
                    }
                </div>
            </div>
            <div className="fri h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                <div className="h-[386px] mx-[4px] flex flex-col items-center">
                    {Array.from({ length: fri }, (_, index) => (
                        <TimeBox inTime = "10:00 AM" outTime= "9:00 PM" index={index} />
                    ))}
                    {
                        (fri < 5) && 
                        <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[fri]} ${colorHover[fri]}`} onClick={handleOpenNoti}>
                            <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                        </div>
                    }
                </div>
            </div>
            <div className="sat h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                <div className="h-[386px] mx-[4px] flex flex-col items-center">
                    {Array.from({ length: sat }, (_, index) => (
                        <TimeBox inTime = "10:00 AM" outTime= "9:00 PM" index={index} />
                    ))}
                    {
                        (sat < 5) && 
                        <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[sat]} ${colorHover[sat]}`} onClick={handleOpenNoti}>
                            <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                        </div>
                    }
                </div>
            </div>
            <div className="sun h-[394px] flex flex-col justify-center items-center">
                <div className="h-[386px] mx-[4px] flex flex-col items-center">
                    {Array.from({ length: sun }, (_, index) => (
                        <TimeBox inTime = "10:00 AM" outTime= "9:00 PM" index={index} />
                    ))}
                    {
                        (sun < 5) && 
                        <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[sun]} ${colorHover[sun]}`} onClick={handleOpenNoti}>
                            <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                        </div>
                    }
                </div>
            </div>
        </div>
    )
}

export default Scheduler;
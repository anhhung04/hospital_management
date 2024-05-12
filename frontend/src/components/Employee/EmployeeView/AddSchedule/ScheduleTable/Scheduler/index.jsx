import { useState, useEffect } from "react"
import TimeBox from "../TimeBox";
function Scheduler({handleOpenAddScheduler, emp, newSche, dataDone}) {
    const [weekDates, setWeekDates] = useState(getWeekDates(new Date()));
    const [weekSche, setWeekSche] = useState({});
    const [initialDay, setInitialDay] = useState();
    const [mon, setMon] = useState(0);
    const [tue, setTue] = useState(0);
    const [wed, setWed] = useState(0);
    const [thu, setThu] = useState(0);
    const [fri, setFri] = useState(0);
    const [sat, setSat] = useState(0);
    const [sun, setSun] = useState(0);
    const colorHover =["hover:bg-[#B3D8F5]", "hover:bg-[#B3F5C1]", "hover:bg-[#FDFFB6]", "hover:bg-[#F9C68A]", "hover:bg-[#FA9189]"];
    const colorFocus =["bg-[#D6F6FF]", "bg-[#E1FBE6]", "bg-[#FEFFDB]", "bg-[#FCE2C5]", "bg-[#FCC8C4]"];
    const [addInDay, setAddInDay] = useState();
    const empId = emp.id;
    const handleDay = (day) => {
        handleOpenAddScheduler(weekDates[day]);
        setAddInDay(day);
        if (day === 0 && mon < 5) {
            setMon(mon + 1);
        }
        else if (day === 1 && tue < 5) {
            setTue(tue + 1);
        }
        else if (day === 2 && wed < 5) {
            setWed(wed + 1);
        }
        else if (day === 3 && thu < 5) {
            setThu(thu + 1);
        }
        else if (day === 4 && fri < 5) {
            setFri(fri + 1);
        }
        else if (day === 5 && sat < 5) {
            setSat(sat + 1);
        }
        else if (day === 6 && sun < 5) {
            setSun(sun + 1);
        }
    }

    useEffect(() => {
        if (dataDone) {
            initialDay[addInDay].push(newSche);
        }
    }, [dataDone])

    useEffect(() => {
        fetch(`/api/employees/${empId}/event/list`, {
            method: "GET",
        })
        .then((response) => response.json())
        .then((data) => {
            setWeekSche(data);
            setInitialDay(countEventsForWeek(weekDates, data));
        })
        .catch((error) => console.error('Error fetching employee scheduler:', error));
}, []);

    useEffect(() => {
        if (initialDay) {
            setMon(initialDay[0].length);
            setTue(initialDay[1].length);
            setWed(initialDay[2].length);
            setThu(initialDay[3].length);
            setFri(initialDay[4].length);
            setSat(initialDay[5].length);
            setSun(initialDay[6].length);
        }
    }, [initialDay])
    

    return (
        <div className="flex flex-col justify-center items-center w-full">
            <div className="date w-[958px] mb-[4px]">
                    <div className="px-[76px] pt-[20px] header flex justify-between">
                        <p className="text-[#032B91] text-2xl font-semibold leading-9 w-[35px] flex justify-center">CN</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9 w-[35px] flex justify-center">T2</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9 w-[35px] flex justify-center">T3</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9 w-[35px] flex justify-center">T4</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9 w-[35px] flex justify-center">T5</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9 w-[35px] flex justify-center">T6</p>
                        <p className="text-[#032B91] text-2xl font-semibold leading-9 w-[35px] flex justify-center">T7</p>
                    </div>
                    <div className="px-[76px] w-[958px] header flex justify-between">
                        {weekDates.map(date => (
                            <div className="flex justify-center w-[35px]">
                                <p className="text-[#032B91] text-2xl font-semibold leading-9">{new Date(date).getDate()}</p>
                            </div>
                        ))
                        }
                    </div>
            </div>
            <div className="flex justify-center w-full mb-[12px]">
                <div className="mon h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mr-[4px] flex flex-col items-center">
                        {
                            (mon > 0) &&  
                            initialDay[0].map((sche, index) => (
                                <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                            ))

                        }
                        {
                            (mon < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[mon]} ${colorHover[mon]}`} onClick={() => handleDay(0)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="tue h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (tue > 0) &&  
                            initialDay[1].map((sche, index) => (
                                <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                            ))

                        }
                        {
                            (tue < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[tue]} ${colorHover[tue]}`} onClick={() => handleDay(1)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="wed h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (wed > 0) &&  
                            initialDay[2].map((sche, index) => (
                                <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                            ))

                        }
                        {
                            (wed < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[wed]} ${colorHover[wed]}`} onClick={() => handleDay(2)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="thu h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (thu > 0) &&  
                            initialDay[3].map((sche, index) => (
                                <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                            ))

                        }
                        {
                            (thu < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[thu]} ${colorHover[thu]}`} onClick={() => handleDay(3)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="fri h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (fri > 0) &&  
                            initialDay[4].map((sche, index) => (
                                <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                            ))

                        }
                        {
                            (fri < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[fri]} ${colorHover[fri]}`} onClick={() => handleDay(4)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="sat h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (sat > 0) &&  
                            initialDay[5].map((sche, index) => (
                                <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                            ))

                        }
                        {
                            (sat < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[sat]} ${colorHover[sat]}`} onClick={() => handleDay(5)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="sun h-[394px] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (sun > 0) &&  
                            initialDay[6].map((sche, index) => (
                                <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                            ))

                        }
                        {
                            (sun < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[sun]} ${colorHover[sun]}`} onClick={() => handleDay(6)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
            </div>
        </div>
    )
}

function formatDate(date) {
    const month = date.getMonth() + 1; 
    const day = date.getDate();
    const year = date.getFullYear();
    return `${month.toString().padStart(2, '0')}/${day.toString().padStart(2, '0')}/${year}`;
  }
  
  function getWeekDates(today) {
    const weekDates = [];
    const currentDay = today.getDay();
    const startDate = new Date(today);
    startDate.setDate(today.getDate() - currentDay);
    const endDate = new Date(today);
    endDate.setDate(today.getDate() + (6 - currentDay));
    for (let date = new Date(startDate); date <= endDate; date.setDate(date.getDate() + 1)) {
      weekDates.push(formatDate(new Date(date)));
    } 
    return weekDates;
  }

  function countEventsForWeek(weekDates, weekSche) {
    const eventCounts = [];
    for (const date of weekDates) {
    if (weekSche.hasOwnProperty(date)) {
        eventCounts.push(weekSche[date]);
    } else {
        eventCounts.push([]);
      }
    }
    return eventCounts;
  }
  

export default Scheduler;
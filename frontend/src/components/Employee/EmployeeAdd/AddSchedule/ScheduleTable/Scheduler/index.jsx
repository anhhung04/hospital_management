import { useState, useEffect } from "react"
import TimeBox from "../TimeBox";
import apiCall from "../../../../../../utils/api";
import PropTypes from 'prop-types';
Scheduler.propTypes = {
    handleOpenAddScheduler: PropTypes.func,
    eventList: PropTypes.object,
    setWeek: PropTypes.func,
    empId: PropTypes.string,
    setDelete: PropTypes.func
};
function Scheduler({handleOpenAddScheduler, eventList, setWeek, empId, setDelete}) {
    const weekDates = getWeekDates(new Date());
    const [initialDay, setInitialDay] = useState([]);
    const [tue, setTue] = useState(0);
    const [wed, setWed] = useState(0);
    const [thu, setThu] = useState(0);
    const [fri, setFri] = useState(0);
    const [sat, setSat] = useState(0);
    const [sun, setSun] = useState(0);
    const [mon, setMon] = useState(0);
    const colorHover =["hover:bg-[#B3D8F5]", "hover:bg-[#B3F5C1]", "hover:bg-[#FDFFB6]", "hover:bg-[#F9C68A]", "hover:bg-[#FA9189]"];
    const colorFocus =["bg-[#D6F6FF]", "bg-[#E1FBE6]", "bg-[#FEFFDB]", "bg-[#FCE2C5]", "bg-[#FCC8C4]"];
    const [deleteDate, setDeleteDate] = useState({});
    const [deletePopup, setDeletePopup] = useState(false);
    const [eventId, setEventId] = useState();
    const [notiPopup, setNotiPopup] = useState(false);

    const handleDay = (day) => {
        handleOpenAddScheduler(weekDates[day]);
    }

    const handleOpen = (id) => {
        setEventId(id);
        setDeletePopup(true);
    }


    useEffect(() => {
        if (eventId) {
            apiCall({            
                endpoint: `/api/employee/${empId}/event/${eventId}`,
                method: "GET"
            })
            .then((data) => {
                console.log(data);
                setDeleteDate(data.data);
            })
        }

    }, [eventId, empId])

    const deleteEvent = () => {
        console.log("empId", empId);
        console.log("eventId", eventId);
            apiCall({            
                endpoint: `/api/employee/${empId}/event/${eventId}/delete`,
                method: "DELETE"
            })
            .then((data) => {
                console.log(data);
            })
        setDelete(true);
        setDeletePopup(false);
        setNotiPopup(true)

        }


    useEffect(() => {
        setWeek(weekDates[0], weekDates[6]);
    }, [weekDates])

    useEffect(() => {
        setInitialDay(countEventsForWeek(weekDates, eventList));
      }, [weekDates, eventList]);


    useEffect(() => {
        if (initialDay) {
            setSun(initialDay[0]?.length);
            setMon(initialDay[1]?.length);
            setTue(initialDay[2]?.length);
            setWed(initialDay[3]?.length);
            setThu(initialDay[4]?.length);
            setFri(initialDay[5]?.length);
            setSat(initialDay[6]?.length);
        }
    }, [initialDay])
    

    return (
        <div className="flex flex-col justify-center items-center w-full">
            {   deletePopup &&
                <div className="fixed inset-0 z-[1] flex items-center justify-center bg-black bg-opacity-50">
                    <div className="popup w-[769px] h-[376px] p-[24px] bg-white shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] rounded-[32px] fixed z-[2] left-[33%] top-[28%]">
                        <div className="header flex justify-between">
                                <p className="text-black text-2xl font-semibold leading-9">Xoá lịch làm việc</p>
                                <button onClick={() => setDeletePopup(false)} className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid">
                                    <img src="/images/xbutton.png"/>
                                </button>
                        </div>
                        <form action="">
                            <div className="first-section flex mt-[12px] justify-between">
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Giờ bắt đầu
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <input className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="7:00:00" disabled  value={deleteDate.begin_time}/><br/>
                                </div>
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Giờ kết thúc
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <input className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="11:00:00" disabled  value={deleteDate.end_time}/><br/>
                                </div>
                            </div>
                            <div className="second-section flex mt-[12px] justify-between">
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Ngày
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <input className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="date" disabled  value={deleteDate.begin_date}/><br/>
                                </div>
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Lặp lại
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <select className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" disabled value={deleteDate.frequency}>
                                        <option value="" disabled selected>Chọn tần suất</option>
                                        <option value="WEEKLY">Hằng tuần</option>
                                        <option value="SINGLE">Không bao giờ</option>
                                    </select>
                                </div>
                            </div>
                        </form>
                        <div className="footer flex justify-end">
                                <button onClick={() => setDeletePopup(false)} className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px]">
                                    <h5 className="text-[#032B91] text-2xl font-semibold leading-9">Hủy</h5>
                                </button>
                                <button onClick={deleteEvent} className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] border-[2px] border-solid bg-[#032B91]">
                                    <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">Xóa</h5>
                                </button>
                        </div>
                    </div>
                </div>

            }
            {
                notiPopup && 
                <div className="w-[623px] h-fit bg-white shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] rounded-[32px] fixed z-[10] left-[38%] top-[35%] p-[24px] flex flex-col">
                    <div className="header flex justify-between w-full">
                        <div className="content">
                            <p className="text-black text-2xl font-semibold leading-9">Xóa thành công</p>
                        </div>
                        <div>
                            <button onClick={() => {setNotiPopup(false); setDelete(false);}} className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid">
                                <img src="/images/xbutton.png"/>
                            </button>
                        </div>
                    </div>
                    <div className="body flex flex-col w-full p-[24px] items-center">
                        <div>
                            <img src="/images/Success.png" className="pb-[24px]"/>
                        </div>
                        <div>
                            <div className="flex flex-col items-center">
                                <p className="text-black font-medium leading-6">Xóa ca làm việc thành công.</p>
                            </div>
                        </div>
                    </div>
                    <div className="button-section flex justify-end">
                        <button className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] border-[2px] border-solid bg-[#032B91]" onClick={() => {setNotiPopup(false); setDelete(false);}}>
                            <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">OK</h5>
                        </button>
                    </div>
                </div>
            }
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
                        {weekDates.map((date, index) => (
                            <div key = {index} className="flex justify-center w-[35px]">
                                <p className="text-[#032B91] text-2xl font-semibold leading-9">{new Date(date).getDate()}</p>
                            </div>
                        ))
                        }
                    </div>
            </div>
            <div className="flex justify-center w-full mb-[12px]">
                <div className="sun h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mr-[4px] flex flex-col items-center">
                        {
                            (sun > 0) &&  
                            initialDay[0].slice(0,5).map((sche, index) => (
                                <div key={index} className="hover:cursor-pointer" onClick={() => handleOpen(sche.id)}>
                                    <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                                </div>
                            ))

                        }
                        {
                            (sun < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[sun]} ${colorHover[sun]}`} onClick={() => handleDay(0)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="mon h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (mon > 0) &&  
                            initialDay[1].slice(0,5).map((sche, index) => (
                                <div key={index} className="hover:cursor-pointer" onClick={() => handleOpen(sche.id)}>
                                    <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                                </div>                       
                            ))

                        }
                        {
                            (mon < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[mon]} ${colorHover[mon]}`} onClick={() => handleDay(1)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="tue h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (tue > 0) &&  
                            initialDay[2].slice(0,5).map((sche, index) => (
                                <div key={index} className="hover:cursor-pointer" onClick={() => handleOpen(sche.id)}>
                                    <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                                </div>                         
                                ))

                        }
                        {
                            (tue < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[tue]} ${colorHover[tue]}`} onClick={() => handleDay(2)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="wed h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (wed > 0) &&  
                            initialDay[3].slice(0,5).map((sche, index) => (
                                <div key={index} className="hover:cursor-pointer" onClick={() => handleOpen(sche.id)}>
                                    <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                                </div>                            
                                ))

                        }
                        {
                            (wed < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[wed]} ${colorHover[wed]}`} onClick={() => handleDay(3)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="thu h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (thu > 0) &&  
                            initialDay[4].slice(0,5).map((sche, index) => (
                                <div key={index} className="hover:cursor-pointer" onClick={() => handleOpen(sche.id)}>
                                    <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                                </div>                          
                                 ))

                        }
                        {
                            (thu < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[thu]} ${colorHover[thu]}`} onClick={() => handleDay(4)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="fri h-[394px] border-r-2 border-solid border-[#A6BFFD] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (fri > 0) &&  
                            initialDay[5].slice(0,5).map((sche, index) => (
                                <div key={index} className="hover:cursor-pointer" onClick={() => handleOpen(sche.id)}>
                                    <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                                </div>                          
                                 ))

                        }
                        {
                            (fri < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[fri]} ${colorHover[fri]}`} onClick={() => handleDay(5)}>
                                <p className="text-[#032B91] text-xs font-medium leading-18">+ Thêm</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="sat h-[394px] flex flex-col justify-center items-center">
                    <div className="h-[386px] mx-[4px] flex flex-col items-center">
                        {
                            (sat > 0) &&  
                            initialDay[6].slice(0,5).map((sche, index) => (
                                <div key={index} className="hover:cursor-pointer" onClick={() => handleOpen(sche.id)}>
                                    <TimeBox inTime = {sche.begin_time} outTime= {sche.end_time} index={index} />
                                </div>                         ))

                        }
                        {
                            (sat < 5) && 
                            <div className={`w-[120px] h-[70px] rounded-[10px] flex items-center justify-center ${colorFocus[sat]} ${colorHover[sat]}`} onClick={() => handleDay(6)}>
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
    return `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
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
        console.log("date", date);
    if (date in weekSche) {
        eventCounts.push(weekSche[date]);
    } else {
        eventCounts.push([]);
      }
    }
    return eventCounts;
  }
  

export default Scheduler;

import { useState, useEffect } from "react";
import Calendar from "./Calendar";
import ScheduleTable from "./ScheduleTable";

function AddSchedule({emp}) {
    const [showAddPopup, setShowAddPopup] = useState(false);
    const [newSche, setNewSche] = useState({
        begin_time: "",
        end_time: "",
        frequency: "",
        begin_date: ""
    });
    const [dataDone, setDataDone] = useState(false);
    const [notiPopup, setNotiPopup] = useState(false);
    const [addDay, setAddDay] = useState();
    const empId = emp.id;

    useEffect(() => {
        if (dataDone) {
            fetch(`/api/employees/${empId}/event/create`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(newSche),
            })
            .then((response) => response.json())
            .then((data) => {
                console.log("Scheduler Employee created:", data);
            })
            .catch((error) => console.error('Error creating scheduler:', error));
        }
    }, [dataDone]);


    const handleOpenAddScheduler = (day) => {
        setAddDay(day);
        setNewSche({...newSche, ["begin_date"]: day});
        setShowAddPopup(true);
    }

    const handleCloseAddScheduler = () => {
        setShowAddPopup(false);
    }
    
    const handleChangeValue = (field, value) => {
        setNewSche({...newSche, [field]: value});
    }

    const handleNoti = () => {
        if (Object.values(newSche).every(value => value !== null && value !== "")) {
            setDataDone(true);
            setShowAddPopup(false);
            setNotiPopup(true);
        }
        else {
            setDataDone(false);
            setNotiPopup(true);
        }
    }
    console.log(newSche);

    return (
        <div>
            {
                showAddPopup && 
                <div className="popup w-[769px] h-[376px] p-[24px] bg-white shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] rounded-[32px] fixed z-[1] left-[33%] top-[28%]">
                    <div>
                        <div className="header flex justify-between">
                                <p className="text-black text-2xl font-semibold leading-9">Thêm lịch làm việc mới</p>
                                <button onClick={() => setShowAddPopup(false)} className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid">
                                    <img src="/images/xbutton.png"/>
                                </button>
                        </div>
                        <form action="">
                            <div className="first-section flex mt-[12px] justify-between">
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Giờ bắt đầu
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <input className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="7:00 AM" onChange={(e) => handleChangeValue("begin_time", e.target.value)}/><br/>
                                </div>
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Giờ kết thúc
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <input className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="11:00 AM" onChange={(e) => handleChangeValue("end_time", e.target.value)}/><br/>
                                </div>
                            </div>
                            <div className="second-section flex mt-[12px] justify-between">
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Ngày
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <input className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="date" value={addDay} disabled/><br/>
                                </div>
                                <div className="flex flex-col justify-start">
                                    <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Lặp lại
                                        <span className="text text-[#F00]">*</span>
                                    </label>
                                    <select className="w-[340px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="Nguyễn Văn A" onChange={(e) => handleChangeValue("frequency", e.target.value)}>
                                        <option value="" disabled selected>Chọn tần suất</option>
                                        <option value="Hằng tuần">Hằng tuần</option>
                                        <option value="Không bao giờ">Không bao giờ</option>
                                    </select>
                                </div>
                            </div>
                        </form>
                        <div className="footer flex justify-end">
                                <button onClick={() => setShowAddPopup(false)} className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px]">
                                    <h5 className="text-[#032B91] text-2xl font-semibold leading-9">Hủy</h5>
                                </button>
                                <button onClick={handleNoti} className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] border-[2px] border-solid bg-[#032B91]">
                                    <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">Thêm</h5>
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
                            {dataDone && <p className="text-black text-2xl font-semibold leading-9">Thêm thành công</p>}
                            {!dataDone && <p className="text-black text-2xl font-semibold leading-9">Thêm không thành công</p>}
                        </div>
                        <div>
                            <button onClick={() => {setNotiPopup(false); setDataDone(false);}} className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid">
                                <img src="/images/xbutton.png"/>
                            </button>
                        </div>
                    </div>
                    <div className="body flex flex-col w-full p-[24px] items-center">
                        <div>
                            {dataDone && <img src="/images/Success.png" className="pb-[24px]"/>}
                            {!dataDone && <img src="/images/Failed.png" className="pb-[24px]"/>}
                        </div>
                        <div>
                            {dataDone &&
                            <div className="flex flex-col items-center">
                                <p className="text-black font-medium leading-6">Ca làm việc mới được thêm thành công.</p>
                            </div>
                            }
                            {!dataDone &&
                            <div className="flex flex-col items-center">
                                <p className="text-black font-medium leading-6">Ca làm việc không hợp lệ. Vui lòng điền lại</p>
                            </div>
                            }
                        </div>
                    </div>
                    <div className="button-section flex justify-end">
                        <button className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] border-[2px] border-solid bg-[#032B91]" onClick={() => {setNotiPopup(false); setDataDone(false);}}>
                            <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">OK</h5>
                        </button>
                    </div>
                </div>
            }
            <div className="my-[40px] mx-[60px] flex justify-between">
                <Calendar/>
                <div className="info-section flex flex-col pt-[6px]">
                    <div>
                        <p className="text-black text-xl font-medium leading-8">Trạng thái</p>
                        <div className="flex items-center px-[8px] w-[586px] h-[42px] mt-[4px] text-[#9AA6B4] font-medium leading-6 border rounded-[5px] border-solid border-[#9AA6B4]">Trong giờ làm</div>
                    </div>
                    <div className="mt-[36px]">
                        <p className="text-black text-xl font-medium leading-8">Ca làm hiện tại</p>
                        <div className="flex items-center px-[8px] w-[586px] h-[42px] mt-[4px] text-[#9AA6B4] font-medium leading-6 border rounded-[5px] border-solid border-[#9AA6B4]">11:00 AM - 1:00 PM</div>
                    </div>
                </div>
            </div>
            <div className="mx-[60px]">
                <ScheduleTable handleOpenAddScheduler = {handleOpenAddScheduler} emp = {emp} newSche = {newSche} dataDone = {dataDone}/>
            </div>
        </div>

    )
}

function formatDate(date) {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0'); 
    const day = date.getDate().toString().padStart(2, '0');
    return `${month}/${day}/${year}`;
  }
  

export default AddSchedule;

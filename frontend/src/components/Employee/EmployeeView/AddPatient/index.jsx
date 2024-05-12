import { useState, useRef } from "react";
import "./style.css" 
import FormList from "./FormList";
import ListBar from "../../Component/ListBar/ListBar";

function AddPatient() {
    const [patientList, setPatientList] = useState(1);
    const [showPopup, setShowPopup] = useState(false);
    const popupRef = useRef(null);
    const handleOpen = () => {
        setShowPopup(true);
    }
    const handleClose = () => {
        setShowPopup(false);
    }
    const props = [
        {
            progess: '#000001',
            patient: 'Nguyen Van A',
            date: '30/04/2024',
            time: '09:00 AM',
            status: 'Benh'
        },
        
        {
            progess: '#000002',
            patient: 'Nguyen Van A',
            date: '30/04/2024',
            time: '09:00 AM',
            status: 'Benh'
        },

        {
            progess: '#000003',
            patient: 'Nguyen Van A',
            date: '30/04/2024',
            time: '09:00 AM',
            status: 'Benh'
        },

        {
            progess: '#000004',
            patient: 'Nguyen Van A',
            date: '30/04/2024',
            time: '09:00 AM',
            status: 'Benh'
        },

        {
            progess: '#000005',
            patient: 'Nguyen Van A',
            date: '30/04/2024',
            time: '09:00 AM',
            status: 'Benh'
        },

        {
            progess: '#000004',
            patient: 'Nguyen Van A',
            date: '30/04/2024',
            time: '09:00 AM',
            status: 'Benh'
        },

        {
            progess: '#000005',
            patient: 'Nguyen Van A',
            date: '30/04/2024',
            time: '09:00 AM',
            status: 'Benh'
        }
    ];

    return (
        <div className="table-conttainer w-full px-[60px] py-[40px] ">
            {
                showPopup && 
                <div className="popup w-[500px] h-[352px] p-[24px] bg-white shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] rounded-[32px] fixed z-[1] left-[40%] top-[28%]" ref={popupRef}>
                    <div>
                        <div className="header flex justify-between">
                                <p className="text-black text-2xl font-semibold leading-9">Thêm bệnh nhân</p>
                                <button onClick={handleClose} className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid">
                                    <img src="/images/xbutton.png"/>
                                </button>
                        </div>
                        <form action="">
                            <div className="flex flex-col justify-start mt-[12px]">
                                <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Họ và tên
                                    <span className="text text-[#F00]">*</span>
                                </label>
                                <input className="w-full rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="Nguyễn Văn A"/><br/>
                            </div>
                            <div className="flex flex-col justify-start mt-[0px]">
                                <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Mã bệnh nhân
                                </label>
                                <input className="w-full rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="#000001"/><br/>
                            </div>
                        </form>
                        <div className="footer flex justify-end">
                                <button onClick={handleClose} className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px]">
                                    <h5 className="text-[#032B91] text-2xl font-semibold leading-9">Hủy</h5>
                                </button>
                                <button className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] border-[2px] border-solid bg-[#032B91]">
                                    <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">Tìm</h5>
                                </button>
                        </div>
                    </div>
                </div>

            }
            
            <div className="header flex justify-between items-center">
                <div className="left-header flex items-center">
                        <div>
                            <button className="Add-button" onClick={handleOpen}>
                                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" fill="none">
                                <circle className="cir" cx="16" cy="16" r="16" fill="#EFF7FE"/>
                                <path className="plus" fill-rule="evenodd" clip-rule="evenodd" d="M15 7C14.4477 7 14 7.44772 14 8V14H8C7.44772 14 7 14.4477 7 15V17C7 17.5523 7.44772 18 8 18H14V24C14 24.5523 14.4477 25 15 25H17C17.5523 25 18 24.5523 18 24V18H24C24.5523 18 25 17.5523 25 17V15C25 14.4477 24.5523 14 24 14H18V8C18 7.44772 17.5523 7 17 7H15Z" fill="#032B91"/>
                                </svg>
                            </button>
                        </div>
                        <div className="content px-[8px]">
                            <p className="text-[#032B91] text-2xl font-semibold leading-9">Bệnh nhân</p>
                        </div>
                </div>
                <div className="right-header gap-[16px] flex items-center content-end">
                    <div className="w-[203px] h-[44px] bg-[#EFF7FE] flex shrink-0 items-center justify-center">
                        <div className="basis-full flex justify-center">
                            <h6 className="font-sans text-[20px] font-medium leading-[32px] text-[#000] mx-[15px]">All Selected</h6>
                        </div>
                        <div className="w-[60px] h-[44px] flex items-center justify-center border-l-2 border-l-[white] border-solid">
                            <img src="/images/Patient_Garbage.png" alt="icon" className="w-[24px] h-[24px]"/>
                        </div>
                    </div>
                    <div className="w-[237px] h-[42px] flex shrink-0 items-center rounded-full bg-[#EFF7FE] px-[20px] py-[12px]">
                        <div className="font-sans text-[12px] font-normal leading-[18px] text-[#000]">Tìm kiếm</div>
                    </div>
                    <img src="/images/Patient_Sorted.png" alt="sorted" />
                    <img src="/images/Patient_filter.png" alt="filter" />
                </div>

            </div>
            <div className="list my-[20px] h-[350px]">
                <FormList prop={['STT', 'Mã tiến trình', 'Bệnh nhân', 'Ngày thực hiện', 'Giờ thực hiện', 'Tình trạng', 'Chi tiết']}/>
                <div className="list-content flex flex-col justify-between items-center w-full mt-[20px]">
                    {!patientList && <p className="text-black text-[34px] not-italic font-medium leading-[48px] mt-[30px]">Chưa có dữ liệu nào</p>}
                    {patientList && 
                        <div className="w-full flex flex-col gap-[8px]">
                            {props.slice(0, 7).map((uniPatient, index) => (
                                <div className="header flex h-[36px] items-center">
                                    <div className="checkbox ml-[20px] flex items-center">
                                        <input className="flex items-center" type="checkbox"></input>
                                    </div>
                                    <div key={index} className="header-content flex justify-between w-full ml-[34px] mr-[26px] items-center">
                                        <p className="text-black font-normal leading-6">{index + 1}</p>
                                        {Object.keys(uniPatient).map((key) => (
                                            <p key={key} className="text-black font-normal leading-6">{uniPatient[key]}</p>
                                        ))}
                                        <p className="text-[#0544E4] font-normal leading-6">Hồ sơ ↗</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    }
                </div>
            </div>
            <div className="footer">
                {patientList &&
                    <div className='flex items-center justify-between p-[10px] mt-[24px]'>
                        <div>
                            <p className='text-black text-lg font-medium leading-6'>Tổng số lượng: {props.length}</p>
                        </div>
                        <ListBar inForm = {true}/>           
                    </div>
                }
            </div>
        </div>
    )
}

export default AddPatient;
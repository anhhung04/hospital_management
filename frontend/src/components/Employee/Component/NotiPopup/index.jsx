function NotiPopup({content, handleCloseNotiPopup, done, handleAddDone, handleCloseAdd, viewEmp}) {
    return (
        <div>
            <div className="h-fit w-[623px] rounded-[32px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] p-[24px] flex flex-col">
                <div className="header flex justify-between w-full">
                    <div className="content">
                        {content === "success" && <p className="text-black text-2xl font-semibold leading-9">Lưu thành công</p>}
                        {content === "fail" && <p className="text-black text-2xl font-semibold leading-9">Lưu không thành công</p>}
                        {content === "warning" && <p className="text-black text-2xl font-semibold leading-9">Chưa lưu</p>}
                        {content === "alert" && <p className="text-black text-2xl font-semibold leading-9">Cảnh báo</p>}
                    </div>
                        {
                            !done && 
                            <button onClick={handleCloseNotiPopup} className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid">
                                <img src="/images/xbutton.png"/>
                            </button>
                        }
                        {
                            done && 
                            <button onClick={() => {handleCloseNotiPopup(); handleAddDone(true)}} className="w-[32px] h-[32px] bg-white flex justify-center items-center rounded-[10px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] hover:bg-transparent hover:border-[3px] hover:border-[#032B91] hover:border-solid">
                                <img src="/images/xbutton.png"/>
                            </button>
                        }
                    
                </div>
                <div className="body flex flex-col w-full p-[24px] items-center">
                    <div>
                        {content === "success" && <img src="/images/Success.png" className="pb-[24px]"/>}
                        {content === "fail" && <img src="/images/Failed.png" className="pb-[24px]"/>}
                        {(content === "warning" || content === "alert") && <img src="/images/Warning.png" className="pb-[24px]"/>}
                    </div>
                    <div>
                        {content === "success" && done && !viewEmp &&
                            <div className="flex flex-col items-center">
                                <p className="text-black font-medium leading-6">Nhân viên mới được thêm thành công.</p>
                            </div>
                        }
                        {content === "success" && viewEmp &&
                            <div className="flex flex-col items-center">
                                <p className="text-black font-medium leading-6">Sửa nhân viên thành công.</p>
                            </div>
                        }
                        {content === "fail" && <p className="text-black font-medium leading-6">Thông tin không hợp lệ. Vui lòng điền lại.</p>}
                        {content === "warning" &&
                            <div className="flex flex-col items-center">
                                <p className="text-black font-medium leading-6">Nhân viên mới chưa được thêm.</p>
                                <p className="text-black font-medium leading-6">Bạn có chắc muốn hủy thông tin nhân viên mới?</p>
                            </div>
                        }
                        {content === "alert" && 
                            <div className="flex flex-col items-center">
                                <p className="text-black font-medium leading-6">Vui lòng thêm thông tin của nhân viên trước.</p>
                            </div>
                        }
                    </div>
                </div>
                <div className="button-section flex justify-end">
                    <div>
                        {content === "success" && done &&
                            <button className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] border-[2px] border-solid bg-[#032B91]" onClick={() => {handleCloseNotiPopup(); handleAddDone(true)}}>
                                <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">OK</h5>
                            </button>
                        }
                        {((content === "success" && !done) || content === "fail") && 
                        <button className="w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] border-[2px] border-solid bg-[#032B91]" onClick={handleCloseNotiPopup}>
                            <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">OK</h5>
                        </button>
                        }
                        {(content === "warning") && 
                        <div className="flex flex-end gap-[9px]">
                            <button className="w-[60px] h-[52px] flex items-center justify-center mr-[18px]" onClick={handleCloseNotiPopup}>
                                <h5 className="text-2xl font-semibold leading-9 text-[#032B91]">Không</h5>
                            </button>  
                            <button className="w-[120px] h-[52px] flex items-center justify-center rounded-[20px] border-[2px] border-solid bg-[#032B91]" onClick={handleCloseAdd}>
                                <h5 className="text-2xl font-semibold leading-9 text-[#F9FBFF]">Có</h5>
                            </button>  
                        </div>

                        }
                    </div>
                </div>
            </div>
        </div>
    )
};

export default NotiPopup;
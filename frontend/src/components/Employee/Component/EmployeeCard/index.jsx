import { useState } from 'react';
import React from 'react';

function EmployeeCard({isChecked, emp, handleCheck, handleView}) {
    const statusText = ["text-[#00F40A]", "text-[#FFD602]", "text-[#FF2727]"];
    const statusBorder = ["border-[#00F40A]", "border-[#FFD602]", "border-[#FF2727]"];
    let indexColor = 0;

    if (emp.status === "Trống") indexColor = 0;
    else if (emp.status === "Khám bệnh") indexColor = 1;
    else if (emp.status === "Phẫu thuật") indexColor = 2;
    
    return (
        <div className='w-[316px] h-[220px] my-[15px] mx-[15px] rounded-[30px] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]'>
            <div className='image-section relative'>
                <div className='w-full absolute flex justify-between flex-1 px-4 items-center '>
                    <div>
                        <input type='checkbox' checked={isChecked} onChange={(e) => handleCheck(emp.id - 1, e.target.checked)}/>
                    </div>
                    <div className={`border-[3px] ${statusBorder[indexColor]} rounded-[20px] w-[83px] h-[39px] flex justify-center items-center mt-3`}>
                        <p className={`${statusText[indexColor]} text-xs not-italic font-bold leading-[18px]`}>{emp.status || "Trống"}</p>
                    </div>

                </div>
                <img className='' src="/images/DoctorImage.png" alt="EmployeeImage" />
            </div>
            <div className='content-section flex flex-col py-2.5 justify-between'>
                <div className='row-container flex justify-between px-9'>
                    <p className='text-black text-sm not-italic font-medium leading-6'>{emp.type}</p>
                    <p className='text-black text-xs not-italic font-normal leading-[18px]'>Khoa {emp.faculty}</p>
                </div>
                <div className='row-container flex justify-between px-9'>
                    <p className='text-black text-sm not-italic font-medium leading-6'>{emp.lastName + " " + emp.firstName}</p>
                    <p className='text-[#0544E4] text-xs not-italic font-normal leading-[18px]' onClick={() => handleView(emp.id)}>Hồ sơ ↗</p>
                </div>
            </div>
        </div>
    )
  
}

export default EmployeeCard;
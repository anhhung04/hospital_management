import { useState } from 'react';
import React from 'react';

function EmployeeCard({emp, handleView}) {
    const statusText = ["text-[#00F40A]", "text-[#FFD602]", "text-[#FF2727]"];
    const statusBorder = ["border-[#00F40A]", "border-[#FFD602]", "border-[#FF2727]"];
    let indexColor = 2;
    let status = 'Khác';

    if (emp.status === "INACTIVE") {
        indexColor = 0;
        status = 'Trống';
    }
    else if (emp.status === "ACTIVE") {
        indexColor = 1;
        status = 'Khám bệnh';
    }
    else if (emp.status === "PENDING") {
        indexColor = 2;
        status = 'Khác';
    }
    
    return (
        <div className='w-[316px] h-[220px] my-[15px] mx-[15px] rounded-[30px] shadow-[0_4px_15px_0px_rgba(216,210,252,0.64)]'>
            <div className='image-section relative'>
                <div className='w-full absolute flex justify-between flex-1 px-4 items-center '>
                    <div className={`border-[3px] ${statusBorder[indexColor]} rounded-[20px] w-[83px] h-[39px] flex justify-center items-center mt-3`}>
                        <p className={`${statusText[indexColor]} text-xs not-italic font-bold leading-[18px]`}>{status}</p>
                    </div>

                </div>
                <img className='' src="/images/DoctorImage.png" alt="EmployeeImage" />
            </div>
            <div className='content-section flex flex-col py-2.5 justify-between'>
                <div className='row-container flex justify-between px-9'>
                    <p className='text-black text-sm not-italic font-medium leading-6'>{emp.employee_type || "Bác sĩ"}</p>
                    <p className='text-black text-xs not-italic font-normal leading-[18px]'>Khoa {emp.faculty}</p>
                </div>
                <div className='row-container flex justify-between px-9'>
                    <p className='text-black text-sm not-italic font-medium leading-6'>{emp.full_name}</p>
                    <p className='text-[#0544E4] text-xs not-italic font-normal leading-[18px]' onClick={() => handleView(emp.id)}>Hồ sơ ↗</p>
                </div>
            </div>
        </div>
    )
  
}

export default EmployeeCard;
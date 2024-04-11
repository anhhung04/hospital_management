import {useState, useEffect} from 'react'
import React from 'react';
import TableEmployee from "./TableEmployee";
import EmployeeCard from './EmployeeCard';
import InfoTag from './InfoTag';
import ListBar from './ListBar/ListBar';
import AddNew from './AddNew/AddNew';

function EmployeeList() {  
    const [checkedState, setCheckedState] = useState([]);
    const [listEmployeeStatus, setListEmployeeStatus] = useState([]);
    const [isChecked, setIsChecked] = useState(false);
    const [isCheckedAll, setIsCheckedAll] = useState(false);
    const [countChecked, setCountChecked] = useState(0);

    // useEffect(() => {
    //     fetch("api/patients/list", {
    //       method: "GET",
    //       headers: {
    //         "Content-Type": "application/json",
    //       },
    //     })
    //       .then((response) => response.json())
    //       .then((data) => {
    //         setListPatient_Info(data);
    //         setCheckedState(new Array(data.length).fill(false));
    //       })
    //       .catch((error) => console.error('Error fetching patient data:', error));
    //   }, []);

    return (
        <div className="w-full bg-[#EFF7FE] flex items-center flex-col">
            <div className='flex my-[40px] w-[1080px]'>
                    <AddNew/>
                    <InfoTag 
                        title="Nhân viên"
                        value="238"
                        source="/images/EmployeeImage.png"
                    ></InfoTag>
                    <InfoTag 
                        title="Bác sĩ"
                        value="238"
                        source="/images/DoctorImage1.png"
                    ></InfoTag>
                    <InfoTag 
                        title="Y tá"
                        value="238"
                        source="/images/NurseImage1.png"
                    ></InfoTag>
            </div>
            <TableEmployee>
                <div className='flex items-center w-[110px] ml-12 justify-between my-[12px]'>
                    <input type='checkbox'></input>
                    <div>
                        <p className='text-[#200101] text-base not-italic font-medium leading-6'>Chọn tất cả</p>
                    </div>
                </div>
                <div>
                    <div className='flex px-12 py-2 justify-between'>
                        <EmployeeCard></EmployeeCard>
                        <EmployeeCard></EmployeeCard>
                        <EmployeeCard></EmployeeCard>
                    </div>
                    <div className='flex px-12 py-2 justify-between'>
                        <EmployeeCard></EmployeeCard>
                        <EmployeeCard></EmployeeCard>
                        <EmployeeCard></EmployeeCard>
                    </div>
                    <div className='flex px-12 py-2 justify-between'>
                        <EmployeeCard></EmployeeCard>
                        <EmployeeCard></EmployeeCard>
                        <EmployeeCard></EmployeeCard>
                    </div>
                </div>
            </TableEmployee>
            <div className='flex items-center w-[1080px] justify-between p-[10px] mt-[24px]'>
                <div>
                    <p className='text-black text-lg font-medium leading-6'>Tổng số lượng: 238</p>
                </div>
                <ListBar/>
            </div>
        </div>
        
    )
}

export default EmployeeList;
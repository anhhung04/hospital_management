import {useState, useEffect} from 'react'
import React from 'react';

import EmployeeAdd from './EmployeeAdd/EmployeeAdd';
import TableEmployee from "./Component/TableEmployee";
import EmployeeCard from './Component/EmployeeCard';
import InfoTag from './Component/InfoTag';
import ListBar from './Component/ListBar/ListBar';
import AddNew from './Component/AddNew/AddNew';
import EmployeeView from './EmployeeView/EmployeeView';


function EmployeeList() {  
    const [listEmployee, setListEmployee] = useState([]);
    const [listDoctor, setListDoctor] = useState([]);
    const [listNurse, setListNurse] = useState([]);
    const [listOther, setListOther] = useState([]);
    const [displayList, setDisplayList] = useState([]);
    const [isCheckedAll, setIsCheckedAll] = useState(false);
    const [addNewEmp, setAddNewEmp] = useState(false);
    const [pageNumber, setPageNumber] = useState(0);
    const [checkedEmployees, setCheckedEmployees] = useState({});
    const [countChecked, setCountChecked] = useState(0);
    const [filterType, setFilterType] = useState("Tất cả")
    const [addDone, setAddDone] = useState(false);
    const [viewEmp, setViewEmp] = useState(false);
    const [viewEmpId, setViewEmpId] = useState();

    console.log(viewEmp);
    console.log(viewEmpId);

    const handleAddNewEmp = () => {
        setAddNewEmp(true); 
    }

    useEffect(() => {
        if (viewEmpId) {
            setViewEmp(true);
        }
    },[viewEmpId])

    useEffect(() => {
        setPageNumber(0);
        fetch("/api/employees", {
          method: "GET",
        })
          .then((response) => response.json())
          .then((data) => {
            const doctor = Object.values(data.employees).filter(emp => emp.type === "Bác sĩ");
            const nurse = Object.values(data.employees).filter(emp => emp.type === "Y tá");
            const other = Object.values(data.employees).filter(emp => emp.type === "Khác");
            setListEmployee(Object.values(data.employees));
            setListDoctor(doctor);
            setListNurse(nurse);
            setListOther(other);
            setDisplayList(Object.values(data.employees));
          })
          .catch((error) => console.error('Error fetching employee data:', error));
      },[addNewEmp, viewEmp, addDone])

    useEffect(() => {
        setPageNumber(0);
        setCheckedEmployees({});
        setIsCheckedAll(false);
        setAddDone(false);
        if (filterType === "Tất cả") setDisplayList(listEmployee);
        else if (filterType === "Bác sĩ") setDisplayList(listDoctor);
        else if (filterType === "Y tá") setDisplayList(listNurse);
        else setDisplayList(listOther);
    },[filterType])

    const handleCheckAllChange = (event) => {
        setIsCheckedAll(event.target.checked);
        const updatedCheckedEmployees = {};
        displayList.forEach(employee => {
            updatedCheckedEmployees[employee.id - 1] = event.target.checked;
        });
        setCheckedEmployees(updatedCheckedEmployees);
    };

    useEffect(() => {
        let count = 0;
        for (const key in checkedEmployees) {
            if (checkedEmployees[key]) {
                count++;
            }
        }
        setCountChecked(count);
        if (displayList.length !== 0 && count === displayList.length) setIsCheckedAll(true);
    }, [checkedEmployees]);

    const handleEmployeeCardCheckboxChange = (employeeId, isChecked) => {
        setCheckedEmployees(prevState => ({
            ...prevState,
            [employeeId]: isChecked
        }));
        if (isCheckedAll) setIsCheckedAll(false);
    };

    const handlePage = (page) => {
        setPageNumber(page);
    }

    const handleFilterType = (type) => {
        setFilterType(type);
    }

    if (!addNewEmp) {
        if (!viewEmp) {
            return (
                <div className="w-full bg-[#EFF7FE] flex items-center flex-col">
                    <div className='flex my-[40px] w-[1080px]'>
                            <AddNew onClick={handleAddNewEmp}/>
                            <InfoTag 
                                title="Nhân viên"
                                value={listEmployee.length}
                                source="/images/EmployeeImage.png"
                            ></InfoTag>
                            <InfoTag 
                                title="Bác sĩ"
                                value={listDoctor.length}
                                source="/images/DoctorImage1.png"
                            ></InfoTag>
                            <InfoTag 
                                title="Y tá"
                                value={listNurse.length}
                                source="/images/NurseImage1.png"
                            ></InfoTag>
                    </div>
                    <TableEmployee countChecked={countChecked} listLen={displayList.length} filterType={filterType} handleFilterType={handleFilterType}>
                        <div className='flex items-center w-[110px] ml-12 justify-between my-[12px]'>
                            <input type='checkbox' checked={isCheckedAll} onChange={handleCheckAllChange}></input>
                            <div>
                                <p className='text-[#200101] text-base not-italic font-medium leading-6'>Chọn tất cả</p>
                            </div>
                        </div>
                        <div className='flex flex-wrap w-[1080px] px-[21px]'>
                            {
                                displayList.slice(pageNumber*9, ((pageNumber+1) * 9)).map((emp, index) => 
                                    <EmployeeCard key={index} emp = {emp} isChecked={checkedEmployees[emp.id - 1] || false} handleCheck={handleEmployeeCardCheckboxChange} handleView = {(id) => setViewEmpId(id)}/>
                                )
                            }
                        </div>
                    </TableEmployee> 
                    <div className='flex items-center w-[1080px] justify-between p-[10px] mt-[24px]'>
                        <div>
                            <p className='text-black text-lg font-medium leading-6'>Tổng số lượng: {displayList.length}</p>
                        </div>
                        <ListBar pageNumber={pageNumber} handlePage={handlePage}/>
                    </div>
                </div>
            )
        }
        else {
            return (
                <EmployeeView handleCloseView={() => {setViewEmp(false); setViewEmpId(null);}} handleCloseAdd={() => setAddNewEmp(false)} empId = {viewEmpId} handleAddDone={(done) => setAddDone(done)}/>
            )
        }
    }
    else {
        if (addDone) {
            return (
                <EmployeeView handleCloseView={() => {setViewEmp(false); setViewEmpId(null);}} handleCloseAdd={() => setAddNewEmp(false)} empId = {listEmployee.length+1} handleAddDone={(done) => setAddDone(done)}/>
            )
        }
        else {
            return (
                <EmployeeAdd handleCloseAdd={() => setAddNewEmp(false)} handleAddDone = {(done) => setAddDone(done)}/>
            )
        }
        
    }
    
}

export default EmployeeList;
import {useState, useEffect} from 'react'
import React from 'react';

import apiCall from '../../utils/api';
import EmployeeAdd from './EmployeeAdd/EmployeeAdd';
import TableEmployee from "./Component/TableEmployee";
import EmployeeCard from './Component/EmployeeCard';
import InfoTag from './Component/InfoTag';
import ListBar from './Component/ListBar/ListBar';
import AddNew from './Component/AddNew/AddNew';
import EmployeeView from './EmployeeView/EmployeeView';


function EmployeeList() {  
    const [displayList, setDisplayList] = useState([]);
    const [addNewEmp, setAddNewEmp] = useState(false);
    const [pageNumber, setPageNumber] = useState(1);
    const [filterType, setFilterType] = useState('ALL');
    const [addDone, setAddDone] = useState(false);
    const [viewEmp, setViewEmp] = useState(false);
    const [viewEmpId, setViewEmpId] = useState();
    const [quantity, setQuantity] = useState();

    console.log(viewEmp);
    console.log(viewEmpId);


    useEffect(() => {
        if (viewEmpId) {
            setViewEmp(true);
        }
    },[viewEmpId])


      useEffect(() => {
        apiCall({
          endpoint:  filterType === 'ALL'? `/api/employee/list?page=${pageNumber}&employee_per_page=9`
                                         :  `/api/employee/list?type=${filterType}&page=${pageNumber}&employee_per_page=9`,
          method: "GET",
        })
          .then((data) => {
            console.log("My employee",data)
            if(data && data?.data && data.data?.length > 0){
              setDisplayList(data.data);
            }
            else 
              setDisplayList([]);
          })
          .catch((error) => console.error('Error fetching employee data:', error));
      }, [addNewEmp, viewEmp, addDone, filterType, pageNumber]);

      useEffect(() => {
        setPageNumber(1);
      }, [filterType]);

      useEffect(() => {
        apiCall({
          endpoint: `/api/metric/`,
          method: "GET",
        })
          .then((data) => {
            console.log("My employee's number",data)
            if(data && data?.data) {
                setQuantity(data.data);
            }
            else
                setQuantity({});
          })
          .catch((error) => console.error('Error fetching employee data:', error));
      }, []);

    
      if (!addNewEmp) {
        if (!viewEmp) {
            return (
                <div className="w-full bg-[#EFF7FE] flex items-center flex-col">
                    <div className='flex my-[40px] w-[1080px]'>
                            <AddNew onClick={() => setAddNewEmp(true)}/>
                            <InfoTag 
                                title="Nhân viên"
                                value={quantity?.num_employee || 0}
                                source="/images/EmployeeImage.png"
                            ></InfoTag>
                            <InfoTag 
                                title="Bác sĩ"
                                value={quantity?.num_doctors || 0}
                                source="/images/DoctorImage1.png"
                            ></InfoTag>
                            <InfoTag 
                                title="Y tá"
                                value={quantity?.num_nurse || 0}
                                source="/images/NurseImage1.png"
                            ></InfoTag>
                    </div>
                    <TableEmployee filterType={filterType} handleFilterType={(type) => setFilterType(type)}>
                        <div className='flex items-center w-[110px] ml-12 justify-between my-[12px]'>
                        </div>
                        <div className='flex flex-wrap w-[1080px] px-[21px]'>
                            {
                                displayList.map((emp, index) => 
                                    <EmployeeCard key={index} emp = {emp} handleView = {(id) => setViewEmpId(id)}/>
                                )
                            }
                        </div>
                    </TableEmployee> 
                    <div className='flex items-center w-[1080px] justify-between p-[10px] mt-[24px]'>
                        <div>
                            <p className='text-black text-lg font-medium leading-6'>Tổng số lượng: {
                                filterType === 'ALL'? (quantity?.num_employee || 0) :
                                filterType === 'DOCTOR'? (quantity?.num_doctors || 0) :
                                filterType === 'NURSE'? (quantity?.num_nurse || 0) : ((quantity?.num_employee - quantity?.num_doctors - quantity?.num_nurse) || 0)
                            }</p>
                        </div>
                        <ListBar pageNumber={pageNumber} handlePage={(page) => setPageNumber(page)}/>
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
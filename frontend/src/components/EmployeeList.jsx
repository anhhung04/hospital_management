import Shortcurt from "./Shortcurt";
import EmployeeTable from "./EmployeeTable/employeetable";


function EmployeeList() {
    return ( <div className="w-full bg-[#EFF7FE] flex justify-center items-center ">
    <div className="h-[1116px] w-[1080px] flex flex-col items-start gap-[40px]">
      <Shortcurt
        title="Bệnh nhân"
        value={5}
        source="/images/Patient_HeartRateMonitor.png"
      />
      <EmployeeTable />
    </div>
  </div> );
}

export default EmployeeList;
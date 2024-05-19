import Scheduler from "./Scheduler";
import PropTypes from 'prop-types';

ScheduleTable.propTypes = {
    handleOpenAddScheduler: PropTypes.func,
    eventList: PropTypes.object,
    setWeek: PropTypes.func,
    empId: PropTypes.string,
    setDelete: PropTypes.func
};

function ScheduleTable({handleOpenAddScheduler, eventList, setWeek, empId, setDelete}) {
     return (
        <div>
            <div className="header flex items-center">
                <button className="w-[126px] h-[56px] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] rounded-[10px] p-[16px] text-[#032B91] text-xl font-medium leading-8">Hôm nay</button>
                <div className="btn prev px-[36px]">
                    <p className="text-[#032B91] text-2xl font-semibold leading-9">{'<'}</p>
                </div>
                <div className="btn next">
                    <p className="text-[#032B91] text-2xl font-semibold leading-9">{'>'}</p>
                </div>
                <div className="content pl-[36px] text-[#032B91] text-2xl font-semibold leading-9">Tháng 5, 2024</div>
                
            </div>
            <div className="table-container mt-[16px] mb-[38px] w-[958px] h-[512px] rounded-[47px] bg-[#ffffff] shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] flex flex-col justify-center items-center">
                <div className="schedule w-[958px]">
                    <Scheduler handleOpenAddScheduler = {handleOpenAddScheduler} eventList = {eventList}  setWeek = {setWeek} empId={empId} setDelete = {setDelete}/>
                </div>

            </div>
        </div>
    )
}

export default ScheduleTable;

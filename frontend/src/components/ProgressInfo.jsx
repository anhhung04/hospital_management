import PropTypes from 'prop-types';

ProgressInfo.propTypes = {
    keyy: PropTypes.number,
    id: PropTypes.number,
    time: PropTypes.string,
    status: PropTypes.string,
    detailContent: PropTypes.object,
    setIsDetail: PropTypes.func,
    setObjProgress: PropTypes.func,

};


function ProgressInfo(props) {

    function splitDateTime(dateTimeString) {
        const [datePart, timePart] = dateTimeString.split(' ');
        return [datePart, timePart.substr(0, 5)]; // Lấy 5 ký tự đầu tiên của phần thời gian (hh:mm)
      }

    const [date, time] = splitDateTime(props.time);

    // function splitDateTime(dateTimeString) {
    //     // Split the string based on the space character
    //     const [datePart, timePart] = dateTimeString.split(" ");
    
    //     // Further split the time part based on the colon character
    //     const [hour, minute] = timePart.split(":").slice(0, 2); // Take only the first two elements
    
    //     return [datePart, `${hour}:${minute}`];
    // }

    function handleDetail(){
        const [date_treatment, time_treatment] = splitDateTime(props.detailContent.start_treatment);
        const [date_finished, time_finished] = splitDateTime(props.detailContent.end_treatment);
        const newObject={...props.detailContent,
                        "date_performance":date_treatment,
                        "time_performance":time_treatment,
                        "date_finished":date_finished, 
                        "time_finished":time_finished,
                        };
        props.setIsDetail(true);
        props.setObjProgress(newObject);
    }
    return ( <>
    <div className="w-[960px] h-[44px] flex py-[10px] px-[20px] gap-[12px] items-center">
        <input type="checkbox" className="w-[16px] h-[16px] flex-shrink-0" />
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[40px]">00{props.keyy+1}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[132px]">#0000{props.id}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[183px]">{date}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[168px] pr-[30px]">{time}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[145px]">{props.status}</p>
        <p className="font-sans text-[16px] font-[400px] text-right text-[#0544E4] w-[124px]" onClick={()=>{handleDetail()}}>Chi tiết ↗</p>
    </div> 
    </> );
}

export default ProgressInfo;
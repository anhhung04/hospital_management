import PropTypes from 'prop-types';

ProgressInfo.propTypes = {
    keyy: PropTypes.number,
    id: PropTypes.number,
    time: PropTypes.string,
    status: PropTypes.string
};


function ProgressInfo(props) {
    function splitDateTime(dateTimeString) {
        const [datePart, timePart] = dateTimeString.split(' ');
        return [datePart, timePart.substr(0, 5)]; // Lấy 5 ký tự đầu tiên của phần thời gian (hh:mm)
      }
    const [date, time] = splitDateTime(props.time);
    return ( <>
    <div className="w-[960px] h-[44px] flex py-[10px] px-[20px] gap-[12px] items-center">
        <input type="checkbox" className="w-[16px] h-[16px] flex-shrink-0" />
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[40px]">00{props.keyy+1}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[132px]">#0000{props.id}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[183px]">{date}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[168px] pr-[30px]">{time}</p>
        <p className="font-sans text-[16px] font-medium leading-[24px] text-right w-[145px]">{props.status}</p>
        <p className="font-sans text-[16px] font-[400px] text-right text-[#0544E4] w-[124px]">Chi tiết ↗</p>
    </div> 
    </> );
}

export default ProgressInfo;
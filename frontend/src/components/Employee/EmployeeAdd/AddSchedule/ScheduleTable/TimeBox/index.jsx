function TimeBox({ inTime, outTime, index }) {
    let focusColor;
    const colorFocus =["bg-[#B3D8F5]", "bg-[#B3F5C1]", "bg-[#FDFFB6]", "bg-[#F9C68A]", "bg-[#FA9189]"];
    return (
        <div className={`w-[120px] h-[70px] mb-[4px] ${colorFocus[index]} rounded-[10px] flex items-center justify-center`}>
            <div className="content flex flex-col justify-center items-center">
                <p className="text-[#032B91] text-xs font-medium leading-18">{inTime}</p>
                <p className="text-[#032B91] text-xs font-medium leading-18">-</p>
                <p className="text-[#032B91] text-xs font-medium leading-18">{outTime}</p>
            </div>
        </div>
    );
}

export default TimeBox;

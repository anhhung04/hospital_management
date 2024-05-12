function ListBar({ inForm, pageNumber, handlePage }) {
    return (
        <div className="flex w-[220px] justify-between">
            <div className="w-[32px] h-[32px] flex justify-center items-center">
                <img src="/images/LeftArrow.png" alt="LeftArrow" />
            </div>
            <div className="flex justify-between w-full px-[10px]">
                {Array.from({ length: 4 }, (_, index) => (
                    <button key={index} className={`${index === pageNumber? "bg-[#032B91]" : (inForm? "bg-[#EFF7FE]" : "bg-[#FFF]")}  rounded-[7px] w-[32px] h-[32px] flex justify-center items-center`} onClick={() => handlePage(index)}>
                        <p className={`${index === pageNumber? "text-[#F9FBFF]" : "text-[#032B91]"} text-sm font-medium leading-6`}>{index + 1}</p>
                    </button>
                ))}
            </div>
            <div className="w-[32px] h-[32px] flex justify-center items-center">
                <img src="/images/RightArrow.png" alt="RightArrow" />
            </div>
        </div>
    )
}

export default ListBar;

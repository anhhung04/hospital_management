

function Calendar() {
    const today = new Date();
    //This month
    const currentDate = today;
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();
    // useEffect(() => {
    //     const currentYear = currentDate.getFullYear();
    //     const currentMonth = currentDate.getMonth();
    //     if (currentMonth !== 0) {
    //         const firstDayOfThisMonth = new Date(currentYear, currentMonth, 1);
    //         const firstWeekdayOfThisMonth = firstDayOfThisMonth.getDay();
    //         //Previous month
    //         const lastDayOfPrevMonth = new Date(currentYear, currentMonth, 0).getDate();
    //         const datePrevMonth = [];
    //         for (let i = lastDayOfPrevMonth - firstWeekdayOfThisMonth + 1; i <= lastDayOfPrevMonth; i++) {
    //             datePrevMonth.push(i);
    //         }
    //         console.log("last day of prev month", lastDayOfPrevMonth);
    //         console.log(datePrevMonth);
    //     }
    //     if (currentMonth !== 11) {
    //         const lastDayOfThisMonth = new Date(currentYear, currentMonth + 1, 0);
    //         const lastWeekdayOfThisMonth = lastDayOfThisMonth.getDay();
    //         //Next month
    //         const firstDayOfNextMonth = new Date(currentYear, currentMonth + 1, 1).getDate();
    //         const dateNextMonth = [];
    //         for (let i = firstDayOfNextMonth; i < firstDayOfNextMonth + (6 - lastWeekdayOfThisMonth); i++) {
    //             dateNextMonth.push(i);
    //         }
    //         console.log("first day of next month", firstDayOfNextMonth);
    //         console.log(dateNextMonth);
    //     }
    // }, [currentDate])


    return (
        <div>
            <div className="container">
                <div className="calendar">
                    <div className="header flex w-[314px] justify-between mb-[8px] px-[16px]">
                        <div className="month text-[#032B91] text-xl font-medium leading-8">{"Tháng " + (currentMonth+1) + ", " + currentYear}</div>
                        <div className="btns flex">
                            <div className="btn today flex justify-center items-center mr-[12px]">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                                <rect x="3.5" y="5.5" width="17" height="15" rx="1.5" stroke="#032B91"/>
                                <line x1="4" y1="9.5" x2="20" y2="9.5" stroke="#032B91"/>
                                <path d="M7 4V7" stroke="#032B91" strokeLinecap="round"/>
                                <path d="M17 4V7" stroke="#032B91" strokeLinecap="round"/>
                                <path d="M9 15L11 17L14.5 13.5" stroke="#032B91" strokeLinecap="round" strokeLinejoin="round"/>
                            </svg>
                            </div>
                            <div className="btn prev">
                                <p className="fas fa-chevron-left mr-[6px] text-[#032B91] text-xl font-medium leading-8">{'<'}</p>
                            </div>
                            <div className="btn next">
                                <p className="fas fa-chevron-right ml-[6px] text-[#032B91] text-xl font-medium leading-8">{'>'}</p>
                            </div>
                        </div>
                    </div>
                    <div className="w-[314px] h-fit shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)] rounded-[20px] p-[16px]">
                        <div className="weekdays w-full flex justify-between">
                            <div className="day text-black text-sm font-semibold leading-8">Cn</div>
                            <div className="day text-[#032B91] text-sm font-semibold leading-8">T2</div>
                            <div className="day text-[#032B91] text-sm font-semibold leading-8">T3</div>
                            <div className="day text-[#032B91] text-sm font-semibold leading-8">T4</div>
                            <div className="day text-[#032B91] text-sm font-semibold leading-8">T5</div>
                            <div className="day text-[#032B91] text-sm font-semibold leading-8">T6</div>
                            <div className="day text-[#032B91] text-sm font-semibold leading-8">T7</div>
                        </div>
                        <div  className="w-full flex justify-between">
                            <p className="w-[20px] text-[#A6BFFD] text-sm not-itali font-semibold leading-8 flex justify-center">28</p>
                            <p className="w-[20px] text-[#A6BFFD] text-sm not-itali font-semibold leading-8 flex justify-center">29</p>
                            <p className="w-[20px] text-[#A6BFFD] text-sm not-itali font-semibold leading-8 flex justify-center">30</p>
                            <p className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">1</p>
                            <p className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">2</p>
                            <p className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">3</p>
                            <p className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">4</p>
                        </div>
                        <div className="w-full flex justify-between">
                            {Array.from({ length: 7 }, (_, index) => (
                                <p key={index} className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">{index+5}</p>

                            ))}
                        </div>
                        <div className="w-full flex justify-between">
                            {Array.from({ length: 7 }, (_, index) => (
                                <p key={index} className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">{index+12}</p>

                            ))}
                        </div>
                        <div className="w-full flex justify-between">
                            {Array.from({ length: 7 }, (_, index) => (
                                <p key={index} className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">{index+19}</p>

                            ))}
                        </div>
                        <div className="w-full flex justify-between">
                            {Array.from({ length: 5 }, (_, index) => (
                                <p key={index} className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center">{index+26}</p>

                            ))}
                            <p className="w-[20px] text-[#535353] text-sm not-itali font-semibold leading-8 flex justify-center bg-[#BDBDBD]">31</p>
                            <p className="w-[20px] text-[#A6BFFD] text-sm not-itali font-semibold leading-8 flex justify-center">1</p>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Calendar;
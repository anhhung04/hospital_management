import "./style.css"

function AddNew({ onClick }) {
    return (
        <div className="wrapper" onClick={onClick}>
            <div className="default-button w-[98px] h-[98px] bg-[#FFFF] rounded-full gap-[7px] inline-flex flex-start justify-center items-center shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
                <img src='/images/AddNewEmployee.png' alt='AddNewEmployee'/>
            </div>
            <div className="hover-button w-[240px] h-[98px] pl-[20px] bg-[#FFFF] rounded-full inline-flex flex-start items-center shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
                <img src='/images/AddNewEmployee.png' alt='AddNewEmployee'/>
                <div className="flex p-[10px] items-canter">
                    <p className="text-[#032B91] text-lg font-bold leading-6>{props.value}">Nhân viên mới</p>
                </div>
            </div>
        </div>
        
    )
}

export default AddNew;
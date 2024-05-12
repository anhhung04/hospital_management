function FormList({ prop }) {
    return (
        <div className="list-container ">
            <div className="header flex h-[48px] bg-[#CDDBFE] items-center">
                <div className="checkbox ml-[20px] flex items-center">
                    <input className="flex items-center" type="checkbox"></input>
                </div>
                <div className="header-content flex justify-between w-full mx-[20px] items-center">
                        {
                            prop.map(value => (
                                <p className="text-black text-xl font-medium leading-8">{value}</p>
                            ))
                        }
                </div>
            </div>
        </div>
    )
}

export default FormList;

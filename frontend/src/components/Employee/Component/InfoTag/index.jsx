function InfoTag(props) {
    return ( 
    <div className="w-[240px] h-[98px] ml-[40px] bg-[#FFFF] rounded-full gap-[7px] inline-flex flex-start justify-center items-center shadow-[0px_4px_15px_0px_rgba(216,210,252,0.64)]">
        <div className="w-[50px] h-[50px] flex justify-center items-center"><img src= {props.source} alt="logo" /></div>
        {props.value && props.title &&
            <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
                <p className="text-[#7B7B7B] text-lg font-medium leading-6">{props.value}</p>
                <p className="text-[#7B7B7B] text-lg font-bold leading-6;">{props.title}</p>
            </div>
        }
    </div>);
}

export default InfoTag;
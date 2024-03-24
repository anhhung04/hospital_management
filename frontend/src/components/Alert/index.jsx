import { Modal } from "flowbite-react";

let icons = {
  error: "/images/Failed.png",
};

function Alert(props) {
  return (
      <Modal
        show={props.isAlert}
        onClose={props.closeAlert}
        popup
        className="bg-opacity-100 w-[623px] h-[312px] flex my-[20%] mx-[33.156%] flex-col gap-[24px]  p-[24px] justify-center bg-[#FFF] shadow-2xl rounded-[32px]"
      >
    <div className="w-[575px] h-[264px] flex flex-col gap-[24px] ">
    <div className="w-[575px] h-[36px] gap-[8px] flex items-center justify-between ">
        <h5 className="text-[24px] font-semibold leading-[36px] font-sans ">{props.type}</h5>
        <div className="w-[304px] h-[32px] gap-[10px] mr-[0px] flex justify-end items-center ">
            <div className="w-[66px] h-[66px]  " onClick={()=>props.closeAlert()}>
                <img src="/images/Alert_exit_button.png" alt="exit button" className="hover:w-[66px] hover:h-[66px]"/>
            </div>
        </div>
    </div>
    <div className="w-[575px] h-[80px] flex justify-center items-center" >
        <img src={icons[props.icon_type]} alt="" />
    </div>
    <div className="w-[575px] h-[24px] text-center font-base text-[16px] leading-[24px]">{props.message}</div>
    <div className="w-[575px] h-[52px] gap-[18px] flex justify-end items-center ">
        <button className="hover:w-[125px] hover:h-[57px] w-[120px] h-[52px] flex items-center justify-center gap-[10px] rounded-[20px] bg-[#032B91] text-[24px] font-semibold leading-[36px] font-sans text-[#F9FBFF]"
            onClick={()=>props.closeAlert()}
        >OK</button>
    </div>
    </div>
    </Modal>

  );
}

export default Alert;

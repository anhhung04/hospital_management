import PropTypes from 'prop-types';

function Alert(props) {
  let icons = {
    error: "/images/Failed.png",
    success: "/images/Success.png",
    warning: "/images/Warning.png",
  };

  // Function to create the HTML content
  const createMarkup = () => {
    return {__html: props.message}; // Set the message as inner HTML
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-30 backdrop-blur-sm flex justify-center items-center">
      <div className="w-[623px] h-[312px] bg-[#FFF] flex flex-col items-start gap-[24px] rounded-3xl p-[35px] shadow-xl">
        <div className="w-[553px] h-[264px] flex flex-col gap-[13px] ">
          <div className="w-[553px] h-[80px] flex justify-center items-center mt-[15px]">
            <img src={icons[props.icon_type]} alt="" />
          </div>
          <div className="w-[553px] h-[70px] text-center text-[24px] font-semibold leading-[36px] font-sans break-words flex items-center justify-center" dangerouslySetInnerHTML={createMarkup()}></div>
          <div className="w-[553px] h-[52px] gap-[18px] flex justify-end items-center ">
            <button
              className="hover:w-[105px] hover:h-[52px] w-[100px] h-[50px] flex items-center justify-center gap-[10px] rounded-[15px] bg-[#032B91] text-[24px] font-semibold leading-[36px] font-sans text-[#F9FBFF]"
              onClick={props.closeAlert}
            >
              OK
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

Alert.propTypes = {
  icon_type: PropTypes.string, // Replace with the correct type
  message: PropTypes.string,
  closeAlert: PropTypes.func,
};

export default Alert;

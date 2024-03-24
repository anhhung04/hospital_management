import { Modal, Button } from "flowbite-react";

let icons = {
  error: (
    <>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="81"
        height="80"
        viewBox="0 0 81 80"
        fill="none"
        className="mx-auto mb-4 h-14 w-14 text-gray-400 dark:text-gray-200"
      >
        <path
          d="M25.5 24L40.5 39L55.5 54"
          stroke="#F44336"
          strokeWidth="5"
          strokeLinecap="round"
        />
        <path
          d="M25.5 54L40.5 39L55.5 24"
          stroke="#F44336"
          strokeWidth="5"
          strokeLinecap="round"
        />
        <circle cx="40" cy="39.5" r="35" stroke="#F44336" strokeWidth="5" />
      </svg>
    </>
  ),
};

function Alert(props) {
  return (
      <Modal
        show={props.isAlert}
        size="md"
        onClose={props.closeAlert}
        popup
        className="bg-opacity-100 w-[623px] h-[312px] flex my-[20%] mx-[33.156%] gap-[24px] flex-start p-[24px] justify-center bg-[#FFF] shadow-2xl rounded-[32px] "
      >
        <Modal.Header >{props.type}</Modal.Header>
        <Modal.Body>
          <div className="text-center">
            {icons.error}
            <h3 className="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">
              {props.message}
            </h3>
            <div className="flex justify-center gap-4">
              <Button theme={
                {
                  color: {
                    primary:"text-black bg-gray-800 border border-transparent enabled:hover:bg-gray-900 focus:ring-4 focus:ring-gray-300 dark:bg-gray-800 dark:enabled:hover:bg-gray-700 dark:focus:ring-gray-800 dark:border-gray-700"
                  }
                }
              } color="primary" onClick={props.closeAlert} >
                Ok
              </Button>
            </div>
          </div>
        </Modal.Body>
      </Modal>

  );
}

export default Alert;

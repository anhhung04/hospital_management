function Footer() {
    return ( <footer className="flex justify-center items-center border-t-[1px] pt-5 bg-[#BEC6CF] w-full h-full mb-0">
        <div className="w-[840px] h-[116px] inline-flex justify-between gap-[133px] my-[21px]">
            <div className="flex flex-col flex-start gap-[12px] ">
                <div className="w-[112px] h-[57px]">
                    <img src="/images/image.png" alt="logo" />
                </div>
                <div className="font-sans text-[16px] font-[400px] leading-[24px] w-[226px]">Lorem ipsum dolor sit amet consectetur. Egestas at orci.</div>
            </div>
            <div className="flex flex-col flex-start gap-[4px]">
                <h6 className="text-[20px] font-sans font-medium leading-[32px] ">Liên hệ</h6>
                <div className="text-[14px] font-semibold leading-[24px] font-sans">SĐT: 84+ 9615 01846</div>
                <div className="text-[14px] font-semibold leading-[24px] font-sans">Email: hospital@hcmut.edu,vn</div>
                <div className="text-[14px] font-semibold leading-[24px] font-sans">Địa chỉ: Bách Khoa Cơ Sở 2</div>
            </div>
            <div className="flex flex-col flex-start self-end gap-[8px]">
            <div className="flex flex-start gap-[16px]">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M12 0C5.3725 0 0 5.3725 0 12C0 18.6275 5.3725 24 12 24C18.6275 24 24 18.6275 24 12C24 5.3725 18.6275 0 12 0ZM9.0625 16.9738H6.6325V9.15375H9.0625V16.9738ZM7.8325 8.19375C7.065 8.19375 6.56875 7.65 6.56875 6.9775C6.56875 6.29125 7.08 5.76375 7.86375 5.76375C8.6475 5.76375 9.1275 6.29125 9.1425 6.9775C9.1425 7.65 8.6475 8.19375 7.8325 8.19375ZM17.9375 16.9738H15.5075V12.64C15.5075 11.6313 15.155 10.9462 14.2763 10.9462C13.605 10.9462 13.2063 11.41 13.03 11.8563C12.965 12.015 12.9488 12.24 12.9488 12.4638V16.9725H10.5175V11.6475C10.5175 10.6713 10.4862 9.855 10.4537 9.1525H12.565L12.6763 10.2388H12.725C13.045 9.72875 13.8288 8.97625 15.14 8.97625C16.7388 8.97625 17.9375 10.0475 17.9375 12.35V16.9738Z" fill="#0C46B7"/>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M12 0C5.3725 0 0 5.3725 0 12C0 18.6275 5.3725 24 12 24C18.6275 24 24 18.6275 24 12C24 5.3725 18.6275 0 12 0ZM14.8425 8.2925H13.0388C12.825 8.2925 12.5875 8.57375 12.5875 8.9475V10.25H14.8438L14.5025 12.1075H12.5875V17.6838H10.4588V12.1075H8.5275V10.25H10.4588V9.1575C10.4588 7.59 11.5463 6.31625 13.0388 6.31625H14.8425V8.2925Z" fill="#0C46B7"/>
</svg>
            </div>
            <div className="flex font-sans text-[14px] font-semibold leading-[24px]">© 2024 ABC Hospital</div>
            </div>
        </div>
    </footer> );
}

export default Footer;


// <div className="grid grid-cols-3 gap-x-8 w-full px-[300px] mx-auto h-full ">
//             <div className="w-[226px] h-[116px] " >
//                 <div>
//                     <img src="/images/image.png" alt="logo" className="w-[100px] h-[45px]" />
//                 </div>
//                 <p className="font-[400] font-sans text-base">Lorem ipsum dolor sit amet consectetur. Egestas at orci.</p>
//             </div>
//         <div>
//             <h4 className="font-bold text-xl">Liên hệ</h4>
//             <ul>
//                 <li>SĐT:0961501846</li>
//                 <li>Email: hospital@hcmut.edu.vn</li>
//                 <li>Địa chỉ: Thủ Đức, TP.Hồ Chí Minh</li>
//             </ul>
//         </div>
//         <div className="pt-[35px] ">
//             <div className="my-2 p-0">
//             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="inline hover:">
//                 <path d="M12 0C5.3725 0 0 5.3725 0 12C0 18.6275 5.3725 24 12 24C18.6275 24 24 18.6275 24 12C24 5.3725 18.6275 0 12 0ZM9.0625 16.9738H6.6325V9.15375H9.0625V16.9738ZM7.8325 8.19375C7.065 8.19375 6.56875 7.65 6.56875 6.9775C6.56875 6.29125 7.08 5.76375 7.86375 5.76375C8.6475 5.76375 9.1275 6.29125 9.1425 6.9775C9.1425 7.65 8.6475 8.19375 7.8325 8.19375ZM17.9375 16.9738H15.5075V12.64C15.5075 11.6313 15.155 10.9462 14.2763 10.9462C13.605 10.9462 13.2063 11.41 13.03 11.8563C12.965 12.015 12.9488 12.24 12.9488 12.4638V16.9725H10.5175V11.6475C10.5175 10.6713 10.4862 9.855 10.4537 9.1525H12.565L12.6763 10.2388H12.725C13.045 9.72875 13.8288 8.97625 15.14 8.97625C16.7388 8.97625 17.9375 10.0475 17.9375 12.35V16.9738Z" fill="#0C46B7"/>
//             </svg>
//             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="inline mx-4">
//                 <path d="M12 0C5.3725 0 0 5.3725 0 12C0 18.6275 5.3725 24 12 24C18.6275 24 24 18.6275 24 12C24 5.3725 18.6275 0 12 0ZM14.8425 8.2925H13.0388C12.825 8.2925 12.5875 8.57375 12.5875 8.9475V10.25H14.8438L14.5025 12.1075H12.5875V17.6838H10.4588V12.1075H8.5275V10.25H10.4588V9.1575C10.4588 7.59 11.5463 6.31625 13.0388 6.31625H14.8425V8.2925Z" fill="#0C46B7"/>
//             </svg>
//             </div>
//             <p className="font-normal text-[14px]">@2024 Hospital HCMUT</p>
//         </div>
//     </div>
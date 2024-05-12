import { useRef, useState, useEffect } from "react";

function AddInfo({handleChangeValue, emp}) {
    const imgRef = useRef();
    const imgConRef = useRef();

    // const [infoData, setInfoData] = useState(
    //     {
    //         imgURL: null,
    //         lastName: null,
    //         firstName: null,
    //         dob: null,
    //         gender: null,
    //         ssn: null,
    //         phone: null,
    //         address: null,
    //         email: null,
    //         med: null,
    //     }
    // );

    const handleImg = () => {
        const file = imgConRef.current.files[0]; 
        if (file) {
            const imgUrl = URL.createObjectURL(file);
            imgRef.current.src = imgUrl;
            handleChangeValue("imgURL", imgUrl);
        }
    }

    return (
        <div>
            <form className="my-[40px]" id="myForm" encType="multipart/form-data">
                <div className="first-section flex justify-between items-center px-[60px]">
                    <div className="flex flex-col">
                        <p className="text-black text-xl font-medium leading-8">Ảnh đại diện</p>
                        <div className="image-container mt-[4px] w-[450px] h-[164px] border-2 border-dashed border-[#6E7F94] flex flex-col items-center">
                            <div className="w-full flex justify-center h-[130px]">
                                <img className="object-cover" src="/images/DoctorImage.png" ref={imgRef}/>
                            </div>
                            <div className="flex justify-center items-center h-[34px]">
                                <label htmlFor="image" className="text-[#0544E4] text-base font-medium leading-6">Tải ảnh lên</label>
                                <input type="file" id="image" name="image" accept="image/*" style={{ display: 'none' }} onChange={handleImg} ref={imgConRef}/><br/>
                            </div>
                        </div>
                    </div>
                    <div className="flex flex-col justify-between h-[200px]">
                        <div>
                            <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Họ
                                <span className="text text-[#F00]">*</span>
                            </label><br/>
                            <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="Nguyễn" value={emp.lastName} onChange={(e) => handleChangeValue("lastName", e.target.value)}/><br/>
                        </div>
                        <div>
                            <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Tên
                                <span className="text text-[#F00]">*</span>
                            </label><br/>
                            <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="Văn A" value={emp.firstName} onChange={(e) => handleChangeValue("firstName", e.target.value)}/><br/>
                        </div>
                    </div>
                </div> 
                <div className="second-section mt-[40px] flex justify-between items-center px-[60px]">
                    <div>
                        <label htmlFor="dob" className="text text-black text-xl font-medium leading-8">Ngày sinh
                            <span className="dob text-[#F00]">*</span>
                        </label><br/>
                        <input className="w-[450px] rounded-[5px] mt-[4px]" type="date" id="dob" name="dob" value={emp.dob}  onChange={(e) => handleChangeValue("dob", e.target.value)}/><br/>
                    </div>
                    <div>
                        <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Giới tính
                            <span className="text text-[#F00]">*</span>
                        </label><br/>
                        <select className="w-[450px] rounded-[5px] mt-[4px]" id="genders" name="genders" value={emp.gender}  onChange={(e) => handleChangeValue("gender", e.target.value)}>
                            <option value="" disabled selected>Chọn giới tính</option>
                            <option value="Nam">Nam</option>
                            <option value="Nữ">Nữ</option>
                        </select>
                    </div>
                </div>                   
                <div className="third-section mt-[40px] flex justify-between items-center px-[60px]">
                    <div>
                        <label htmlFor="text" className="text text-black text-xl font-medium leading-8">CCCD
                            <span className="text text-[#F00]">*</span>
                        </label><br/>
                        <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="0123456789" value={emp.ssn} onChange={(e) => handleChangeValue("ssn", e.target.value)}/><br/>
                    </div>
                    <div>
                        <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Số điện thoại
                            <span className="text text-[#F00]">*</span>
                        </label><br/>
                        <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="0123456789" value={emp.phone} onChange={(e) => handleChangeValue("phone", e.target.value)}/><br/>
                    </div>
                </div>                   
                <div className="fourth-section mt-[40px] flex justify-between items-center px-[60px]">
                    <div>
                        <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Địa chỉ
                            <span className="text text-[#F00]">*</span>
                        </label><br/>
                        <input className="w-[960px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="268 Lý Thường Kiệt, Phường 14, Quận 10, Thành phố Hồ Chí Minh, Việt Nam"
                            onChange={(e) => handleChangeValue("address", e.target.value)} value={emp.address} /><br/>
                    </div>
                </div>
                <div className="fifth-section mt-[40px] flex justify-between items-center px-[60px]">
                    <div>
                        <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Email
                        </label><br/>
                        <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="nguyenvana@gmail.com" value={emp.email || "Không có"}  onChange={(e) => handleChangeValue("email", e.target.value)}/><br/>
                    </div>
                    <div>
                        <label htmlFor="text" className="text text-black text-xl font-medium leading-8">Thẻ Bảo hiểm y tế
                        </label><br/>
                        <input className="w-[450px] rounded-[5px] mt-[4px]" type="text" id="text" name="text" placeholder="HS0123456789" value={emp.med || "Không có"} onChange={(e) => handleChangeValue("med", e.target.value)}/><br/>
                    </div>
                </div>
            </form>
        </div>
    )
}

export default AddInfo;
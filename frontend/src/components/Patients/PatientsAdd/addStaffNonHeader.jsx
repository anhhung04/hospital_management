import PropTypes from 'prop-types';

AddStaffNonHeader.propTypes = {
    removeStaffAdded: PropTypes.func,
};

function AddStaffNonHeader(props) {
    return ( <div className="w-full h-[48px] inline-flex items-end content-end gap-[10px] col-span-2 ">
    <input className="w-[294px] h-[48px] self-end border-[1px] border-black border-solid flex items-center rounded-[5px]" type="text" placeholder="Họ và tên"/>
    <input className="w-[294px] h-[48px] self-end border-[1px] border-black border-solid flex items-center rounded-[5px]" type="text" placeholder="Họ và tên"/>
    <input className="w-[294px] h-[48px] self-end border-[1px] border-black border-solid flex items-center rounded-[5px]" type="text" placeholder="Hàng động"/>
    <button className="w-[48px] h-[48px] bg-[#EFF7FE] border-[1px] border-solid flex items-center justify-center rounded-md" onClick={props.removeStaffAdded}>
        <img src="/images/Patient_Garbage.png" alt="Garbage" />
    </button>
</div> );
}

export default AddStaffNonHeader;
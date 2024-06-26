import PropTypes from 'prop-types';

FormList.propTypes = {
    prop: PropTypes.arrayOf(PropTypes.string)
};

function FormList({ prop }) {
    return (
        <div className="list-container ">
            <div className="header flex w-[960px] h-[48px] bg-[#CDDBFE] items-center">
                <div className="header-content flex justify-between w-full mx-[20px] items-center">
                        {
                            prop.map(value => (
                                <p key = {value} className="text-black text-xl font-medium leading-8">{value}</p>
                            ))
                        }
                </div>
            </div>
        </div>
    )
}

export default FormList;

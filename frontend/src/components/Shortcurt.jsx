import PropTypes from 'prop-types';

Shortcurt.propTypes = {
    source: PropTypes.string,
    value: PropTypes.string,
    title: PropTypes.string,
};

function Shortcurt(props) {
    return ( <div className="w-[240px] h-[98px] bg-[#FFFF] rounded-full shadow-2xl gap-[7px] inline-flex flex-start justify-center items-center">
    <div className="w-[50px] h-[50px] flex justify-center items-center"><img src= {props.source} alt="logo" className="hover:size-[50px]" /></div>
    <div className="flex p-[10px] flex-col flex-start w-[115px] h-[68px]">
        <h3 className="font-sans text-[18px] font-medium text-left leading-[24px]">{props.value}</h3>
        <h3>{props.title}</h3>
    </div>
</div>);
}

export default Shortcurt;
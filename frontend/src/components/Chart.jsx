// import ApexCharts from 'apexcharts';
import ReactApexChart from 'react-apexcharts';
import PropTypes from 'prop-types';

Chart.propTypes = {
    metricData: PropTypes.array,
};

function Chart({metricData}) {
    const options = {
        colors: ["#1A56DB", "#FDBA8C"],
        series: [
            {
                name: "Patients Per Day",
                color: "#1A56DB",
                data: metricData,
            },
        ],
        chart: {
            type: "bar",
            height: "320px",
            fontFamily: "Inter, sans-serif",
            toolbar: {
                show: false,
            },
        },
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: "70%",
                borderRadiusApplication: "end",
                borderRadius: 8,
            },
        },
        tooltip: {
            shared: true,
            intersect: false,
            style: {
                fontFamily: "Inter, sans-serif",
            },
        },
        states: {
            hover: {
                filter: {
                    type: "darken",
                    value: 1,
                },
            },
        },
        stroke: {
            show: true,
            width: 0,
            colors: ["transparent"],
        },
        grid: {
            show: false,
            strokeDashArray: 4,
            padding: {
                left: 2,
                right: 2,
                top: -14
            },
        },
        dataLabels: {
            enabled: false,
        },
        legend: {
            show: false,
        },
        xaxis: {
            floating: false,
            labels: {
                show: true,
                style: {
                    fontFamily: "Inter, sans-serif",
                    cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
                }
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        yaxis: {
            show: false,
        },
        fill: {
            opacity: 1,
        },
    };

    return (
        <div className="w-full bg-white rounded-[40px] shadow dark:bg-gray-800 p-4 md:p-6">
            <div id="column-chart" >
                <ReactApexChart options={options} series={options.series} type="bar" height={390} width={1050} />
            </div>
        </div>
    );
}

export default Chart;

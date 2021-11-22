var trafficchart = document.getElementById("trafficflow");
var saleschart = document.getElementById("sales");
var saleschart1 = document.getElementById("sales1");
var saleschart2 = document.getElementById("sales2");
var saleschart3 = document.getElementById("sales3");
var saleschart4 = document.getElementById("sales4");
var saleschart5 = document.getElementById("sales5");


// new
var myChart1 = new Chart(trafficchart, {
type: 'line',
data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    datasets: [{
        data: ['1135', '1135', '1140', '1168', '1150', '1145', '1155', '1155', '1150', '1160', '1185', '1190'],
        backgroundColor: "rgba(48, 164, 255, 0.2)",
        borderColor: "rgba(48, 164, 255, 0.8)",
        fill: true,
        borderWidth: 1
    }]
},
options: {
    animation: {
        duration: 2000,
        easing: 'easeOutQuart',
    },
    plugins: {
        legend: {
            display: false,
            position: 'right',
        },
        title: {
            display: true,
            text: 'Number of Visitors',
            position: 'left',
        },
    },
}
});

// new
var myChart2 = new Chart(saleschart, {
type: 'bar',
data: {
    labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    datasets: [{
            label: 'Score',
            data: [localStorage.getItem("frequency0"), localStorage.getItem("frequency1"),localStorage.getItem("frequency2"), localStorage.getItem("frequency3"), 
            localStorage.getItem("frequency4") ,localStorage.getItem("frequency5"), localStorage.getItem("frequency6"), 
            localStorage.getItem("frequency7"), localStorage.getItem("frequency8"),localStorage.getItem("frequency9"), localStorage.getItem("frequency10")],
            backgroundColor: "rgba(76, 175, 80, 0.5)",
            borderColor: "#6da252",
            borderWidth: 1,
    }]
},
options: {
    animation: {
        duration: 2000,
        easing: 'easeOutQuart',
    },
    plugins: {
        legend: {
            display: false,
            position: 'top',
        },
        title: {
            display: true,
            text: 'Number of Students',
            position: 'left',
        },
    },
}
});
var myChart2 = new Chart(saleschart1, {
    type: 'bar',
    data: {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [{
                label: 'Score',
                data: [localStorage.getItem("frequency2_0"), localStorage.getItem("frequency2_1"),localStorage.getItem("frequency2_2"), localStorage.getItem("frequency2_3"), 
                localStorage.getItem("frequency2_4") ,localStorage.getItem("frequency2_5"), localStorage.getItem("frequency2_6"), 
                localStorage.getItem("frequency2_7"), localStorage.getItem("frequency2_8"),localStorage.getItem("frequency2_9"), localStorage.getItem("frequency2_10")],
                backgroundColor: "rgba(76, 175, 80, 0.5)",
                borderColor: "#6da252",
                borderWidth: 1,
        }]
    },
    options: {
        animation: {
            duration: 2000,
            easing: 'easeOutQuart',
        },
        plugins: {
            legend: {
                display: false,
                position: 'top',
            },
            title: {
                display: true,
                text: 'Number of Students',
                position: 'left',
            },
        },
    }
    });



var myChart2 = new Chart(saleschart2, {
    type: 'bar',
    data: {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [{
                label: 'Score',
                data: [localStorage.getItem("frequency3_0"), 
                localStorage.getItem("frequency3_1"),localStorage.getItem("frequency3_2"), localStorage.getItem("frequency3_3"), 
                localStorage.getItem("frequency3_4") ,localStorage.getItem("frequency3_5"), localStorage.getItem("frequency3_6"), 
                localStorage.getItem("frequency3_7"), localStorage.getItem("frequency3_8"),localStorage.getItem("frequency3_9"), 
                localStorage.getItem("frequency3_10")],
                backgroundColor: "rgba(76, 175, 80, 0.5)",
                borderColor: "#6da252",
                borderWidth: 1,
        }]
    },
    options: {
        animation: {
            duration: 2000,
            easing: 'easeOutQuart',
        },
        plugins: {
            legend: {
                display: false,
                position: 'top',
            },
            title: {
                display: true,
                text: 'Number of Students',
                position: 'left',
            },
        },
    }
    });

var myChart2 = new Chart(saleschart3, {
    type: 'bar',
    data: {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [{
                label: 'Score',
                data: [localStorage.getItem("frequency4_0"), localStorage.getItem("frequency4_1"),localStorage.getItem("frequency4_2"), localStorage.getItem("frequency4_3"), 
                localStorage.getItem("frequency4_4") ,localStorage.getItem("frequency4_5"), localStorage.getItem("frequency4_6"), 
                localStorage.getItem("frequency4_7"), localStorage.getItem("frequency4_8"),localStorage.getItem("frequency4_9"), localStorage.getItem("frequency4_10")],
                backgroundColor: "rgba(76, 175, 80, 0.5)",
                borderColor: "#6da252",
                borderWidth: 1,
        }]
    },
    options: {
        animation: {
            duration: 2000,
            easing: 'easeOutQuart',
        },
        plugins: {
            legend: {
                display: false,
                position: 'top',
            },
            title: {
                display: true,
                text: 'Number of Students',
                position: 'left',
            },
        },
    }
    });

var myChart2 = new Chart(saleschart4, {
    type: 'bar',
    data: {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [{
                label: 'Score',
                data: [localStorage.getItem("frequency5_0"), localStorage.getItem("frequency5_1"),localStorage.getItem("frequency5_2"), localStorage.getItem("frequency5_3"), 
                localStorage.getItem("frequency5_4") ,localStorage.getItem("frequency5_5"), localStorage.getItem("frequency5_6"), 
                localStorage.getItem("frequency5_7"), localStorage.getItem("frequency5_8"),localStorage.getItem("frequency5_9"), localStorage.getItem("frequency5_10")],
                backgroundColor: "rgba(76, 175, 80, 0.5)",
                borderColor: "#6da252",
                borderWidth: 1,
        }]
    },
    options: {
        animation: {
            duration: 2000,
            easing: 'easeOutQuart',
        },
        plugins: {
            legend: {
                display: false,
                position: 'top',
            },
            title: {
                display: true,
                text: 'Number of Students',
                position: 'left',
            },
        },
    }
    });

var myChart2 = new Chart(saleschart5, {
type: 'bar',
data: {
    labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    datasets: [{
            label: 'Score',
            data: [localStorage.getItem("frequency6_0"), localStorage.getItem("frequency6_1"),localStorage.getItem("frequency6_2"), localStorage.getItem("frequency6_3"), 
            localStorage.getItem("frequency6_4") ,localStorage.getItem("frequency6_5"), localStorage.getItem("frequency6_6"), 
            localStorage.getItem("frequency6_7"), localStorage.getItem("frequency6_8"),localStorage.getItem("frequency6_9"), localStorage.getItem("frequency6_10")],
            backgroundColor: "rgba(76, 175, 80, 0.5)",
            borderColor: "#6da252",
            borderWidth: 1,
    }]
},
options: {
    animation: {
        duration: 2000,
        easing: 'easeOutQuart',
    },
    plugins: {
        legend: {
            display: false,
            position: 'top',
        },
        title: {
            display: true,
            text: 'Number of Students',
            position: 'left',
        },
    },
}
});


var myChart2 = new Chart(saleschart6, {
    type: 'bar',
    data: {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [{
                label: 'Score',
                data: [localStorage.getItem("frequency0"), localStorage.getItem("frequency1"),localStorage.getItem("frequency2"), localStorage.getItem("frequency3"), 
                localStorage.getItem("frequency4") ,localStorage.getItem("frequency5"), localStorage.getItem("frequency6"), 
                localStorage.getItem("frequency7"), localStorage.getItem("frequency8"),localStorage.getItem("frequency9"), localStorage.getItem("frequency10")],
                backgroundColor: "rgba(76, 175, 80, 0.5)",
                borderColor: "#6da252",
                borderWidth: 1,
        }]
    },
    options: {
        animation: {
            duration: 2000,
            easing: 'easeOutQuart',
        },
        plugins: {
            legend: {
                display: false,
                position: 'top',
            },
            title: {
                display: true,
                text: 'Number of Sales',
                position: 'left',
            },
        },
    }
    });

    


function createItem() {
      localStorage.setObject('grades', '{{grades}}');
      
}
    
function myFunction() {

var bar0  = localStorage.getItem("frequency0");
var bar1 = localStorage.getItem("frequency1");
var bar2 = localStorage.getItem("frequency2");
var bar3 = localStorage.getItem("frequency3");
var bar4 = localStorage.getItem("frequency4");
var bar5 = localStorage.getItem("frequency5");
var bar6 = localStorage.getItem("frequency6");
var bar7 = localStorage.getItem("frequency7");
var bar8 = localStorage.getItem("frequency8");
var bar9 = localStorage.getItem("frequency9");
var bar10 = localStorage.getItem("frequency10");

console.log(bar0);
console.log(bar1);
console.log(bar2);
console.log(bar3);
console.log(bar4);
console.log(bar5);
console.log(bar6);
console.log(bar7);
console.log(bar8);
console.log(bar9);
console.log(bar10);
    
}

var trafficchart = document.getElementById("trafficflow");
var saleschart = document.getElementById("sales");
var performance = document.getElementById("group_performance");
Chart.defaults.font.size = 16;

// new
Chart.defaults.color = "#000000";

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
    labels: [ 'Adj & adv', 'Articles', 'Conditional sentences', 'Endings of nouns&verbs', 'Plural/one', 'Irregular and regular verbs'],
    
    datasets: [{
            label: 'Score',
            data: [localStorage.getItem("avg1"), localStorage.getItem("avg2"),localStorage.getItem("avg3"), localStorage.getItem("avg4"), 
            localStorage.getItem("avg5") ,localStorage.getItem("avg6")],
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
            text: 'Average Score',
            position: 'left',
        },
    },
   
}
});

var myChart3 = new Chart(performance, {

    type: 'bar',
    
    
    data: {
        labels: [ 'AI-Grouping','Average','Alphabetical Order','Group According to ID'],
        
        datasets: [{
                label: 'Distance',
                data: [localStorage.getItem("dist"), localStorage.getItem("overall_dist"),localStorage.getItem("p_name"), localStorage.getItem("p_id")],
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
                text: 'Average Score',
                position: 'left',
            },
        },
       
    }
    });
    
    

function createItem() {
      localStorage.setObject('grades', '{{grades}}');
      
}


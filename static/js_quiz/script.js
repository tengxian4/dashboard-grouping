
var startButton = document.querySelector("#startQuiz");     //Main page start button
var timer = document.querySelector("#timer");   //Timer when quiz starts
var mainContent = document.querySelector("#mainContent");   //Start page content div
var questionEl = document.querySelector("#title");  //card title
var quizContent = document.querySelector("#quizContent");   //Question options div
var resultDiv = document.querySelector("#answer");  //Div for showing answer is correct/wrong
var scoreDiv = document.querySelector("#score");    //Div for Displying final scores when quiz completed


var secondsLeft = 100, questionIndex = 0,correct = 0 ;
var totalQuestions =18;
//var totalQuestions = questions.length;
var question , option1, option2, option3 ,option4 ,ans, previousScores;
var choiceArray = [], divArray = [];
var pattern_questions =[]
var personalizedIndex=[localStorage.getItem("q1"),
localStorage.getItem("q2"),
localStorage.getItem("q3"),
localStorage.getItem("q4"),
localStorage.getItem("q5"),
localStorage.getItem("q6"),
localStorage.getItem("q7"),
localStorage.getItem("q8"),
localStorage.getItem("q9"),
localStorage.getItem("q10"),
localStorage.getItem("q11"),
localStorage.getItem("q12"),
localStorage.getItem("q13"),
localStorage.getItem("q14"),
localStorage.getItem("q15"),
localStorage.getItem("q16"),
localStorage.getItem("q17"),
localStorage.getItem("q18")] //personalized question for each individual


//create buttons for choices
for(var i = 0 ; i < 4 ; i++){
    var dv = document.createElement("div");
    var ch = document.createElement("button");
    ch.setAttribute("data-index",i);
    ch.setAttribute("class","btn btn-primary rounded-pill mb-2");
    choiceArray.push(ch);
    divArray.push(dv);
}

//Create p for showing answer Correct/Wrong
var result = document.createElement("p");
result.setAttribute("class","text-muted font-italic");
resultDiv.appendChild(result);

//Start Quiz function
function startQuiz(){
    
    startTimer();  
    buildQuestion();  

}

//function to start timer when quiz starts
function startTimer(){
    
    var timeInterval = setInterval(function(){

        secondsLeft--;

        timer.textContent = "Time : "+secondsLeft+ " sec";
        
        if(secondsLeft <= 0 || (questionIndex > totalQuestions-1)){
            if (secondsLeft<=0){
                alert('Time out');
            }
            resultDiv.style.display = "none";
            quizContent.style.display = "none";
            viewResult();
            clearInterval(timeInterval);
            timer.textContent = "";
        }

    },1000);
}


function buildQuestion(){
   
    //hides start page content
    questionEl.style.display= "none";
    mainContent.style.display = "none";
    quizContent.style.display= "none";
  
    if(questionIndex > totalQuestions - 1){
        return;
    }
    else{
        ans =  questions[personalizedIndex[questionIndex]].answer;

        //Display Question 
        questionEl.innerHTML = questions[personalizedIndex[questionIndex]].title;
        questionEl.setAttribute("class","text-left");
        questionEl.style.display= "block";

        for(var j = 0 ; j < 4 ; j++){
            var index = choiceArray[j].getAttribute("data-index");
            choiceArray[j].textContent = (+index+1) +". "+questions[personalizedIndex[questionIndex]].choices[index];
            divArray[j].appendChild(choiceArray[j]);
            quizContent.appendChild(divArray[j]);
        }
         
    }
    quizContent.style.display= "block"; // Display options
}

// Event Listener for options buttons
quizContent.addEventListener("click",function(event){
    
    var element = event.target;
    var userAnswer = element.textContent;
    var userOption   = userAnswer.substring(3, userAnswer.length);
      
        if(userOption === ans){
            correct++; 
            pattern_questions.push(questions[personalizedIndex[questionIndex]].topic_id) ;
            resultDiv.style.display = "block"; 
            
            result.textContent = "Correct!"
            
            setTimeout(function(){
                result.textContent = "";
            },500);

        }
        else {
            secondsLeft -= 10;
            
            result.textContent = "Wrong!"
            
            setTimeout(function(){
                result.textContent = "";
            },500);       
        }
        
        questionIndex++;
        buildQuestion();       
});


//Function to show score when quiz completes
function viewResult(){  

    questionEl.innerHTML = "Test Completed!";
    questionEl.style.display= "block";
    
    var s = document.createElement("p");
    s.textContent = "Your final Score : "+correct;
    scoreDiv.appendChild(s);

    var s = document.createElement("p");
    s.textContent = "Topic of correct answered: "+pattern_questions;
    scoreDiv.appendChild(s);

    

    var form = document.createElement("form");      //Create form for storing highscore
    

    var label = document.createElement("label");    //label
    label.textContent = "Please click Submit:";
    //label.textContent = "Enter Name : ";

    /*var text = document.createElement("input");     //textbox for inputting user name
    text.setAttribute("id","nameInput");
    text.setAttribute("class","ml-3");*/

    var scoreButton = document.createElement("button");     //Submit User score
    scoreButton.setAttribute("class","btn btn-primary rounded-pill mb-2 ml-3 mt-2");
    scoreButton.textContent = "Submit";
    
    form.appendChild(label);
    //form.appendChild(text);
    form.appendChild(scoreButton);
    
    localStorage.setItem("pattern_questions",JSON.stringify(pattern_questions));
    /*console.log(pattern_questions);
    
    $.post( "/postmethod", {
        javascript_data: pattern_questions 

    });*/
    
    scoreDiv.appendChild(form);

    scoreButton.addEventListener("click",func);//,storeScores);  //Submit button click event listener calls storeScores()
}




//Start button event listener on start page which starts quiz
startButton.addEventListener("click",startQuiz);


/*function func(event){
    event.preventDefault();
    var xml = new XMLHttpRequest();
    xml.open("POST","{{url_for('func')}}",true); 
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");

    var pattern_questions = JSON.parse(localStorage.getItem("pattern_questions"));

    xml.onload = function(){
        var dataReply = JSON.parse(this.responseText);
        };//endfunction

    dataSend= JSON.stringify({
        'page_data':pattern_questions
    });

    xml.send(dataSend);} */
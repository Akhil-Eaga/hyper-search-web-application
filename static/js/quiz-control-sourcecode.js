
 //Arjun Panicker


// quiz questions
const quiz = [
   {
      q:'Which flag will help remove certain pages from google search result ?',
      options:['-Keyword','+Keyword','*Keyword'],
      answer:0
   },
   {
      q:'Which flag will help you locate instagram handle of Scarlett Johansson?',
      options:['Scarlett Johansson +instagram','Scarlett Johansson @instagram','Scarlett Johansson'],
      answer:1
   },
   {
      q:'Which flag will help you find pages with the EXACT words within search results.',
      options:['"Keyword"','#Keyword#', '-Keyword-'],
      answer:0
   },
   {
      q:'Which method will help you to easily find Angry One Punch Man on google search?',
      options:['one punch man angry','one/punch/man/angry ','one-punch-man-angry '],
      answer:2
   },
   {
      q:'Which flag will help you find a leather phone case on JB Hifi?',
      options:['Leather Phone Case site:jbhifi.com.au','Leather Phone Case link:jbhifi.com.au','Leather Phone Case related:jbhifi.com.au'],
      answer:0
   },
   {
     q:" Which method will help you find news articles from 7news?",
     options:['news find:7news.com.au','news source:7news.com.au','news podcast:7news.com.au'],
     answer:1
   },
   {
     q:'What flag will you use to filter results containing either Milk chocolates or Dark chocolates?',
     options:['Milk chocolates :: Dark chocolates','Milk chocolates OR Dark chocolates','Milk chocolates AND Dark chocolates'],
     answer:1
   },
   {
     q:'Which flag will help you easily find the user manual PDF of your new Samsung Washing Machine?',
     options:['washing-machine-model filetype:pptx site:samsung.com','washing-machine-model datatype:pdf site:samsung.com','washing-machine-model filetype:pdf site:samsung.com'],
     answer:2,
   },
   {
     q:"How will you search music whose lyrics you don't remember?",
     options:['Chorus*lyrics*vocals','Chorus@lyrics@vocals','Chorus#lyrics#vocals'],
     answer:0,
   },
   {
      q:"Which flag will help you find trending topics on twitter easily?",
      options:['#Trending','Trending on Twitter', '#trending @twitter'],
      answer:2,
    }
  ]

// Control Script
const questionNumber = document.querySelector(".question-number");
const questionText = document.querySelector(".question-text");
const optionContainer = document.querySelector(".option-container");
const answersIndicatorContainer = document.querySelector(".answers-indicator");
const instructionBox = document.querySelector(".instruction-box");
const questionsBox = document.querySelector(".questions-box");
const resultBox = document.querySelector(".result-box");
const prevResultBox = document.querySelector(".prev-result-box");
const questionLimit = quiz.length;
let questionCounter = 0;
let currentQuestion;
let availableQuestions = [];
let availableOptions = [];
let correctAnswers = 0;
let attempt = 0;

// push the questions into  availableQuestions Array
function setAvailableQuestions(){
   const totalQuestion = quiz.length;
   for(let i=0; i<totalQuestion; i++){
      availableQuestions.push(quiz[i]);
   }
}

// set question number and question and options
function getNewQuestion(){
   // set question number 
   questionNumber.innerHTML = "Question " + (questionCounter + 1) + " of " + questionLimit;

   // set question text
   // get random question
   const questionIndex = availableQuestions[Math.floor(Math.random() * availableQuestions.length)];
   currentQuestion = questionIndex;
   questionText.innerHTML = currentQuestion.q;
   // get the position of 'questionIndex' from the availableQuestion Array
   const index1= availableQuestions.indexOf(questionIndex);
   // remove the 'questionIndex' from the availableQuestion Array, so that the question does not repeat
   availableQuestions.splice(index1,1);
   // show question img if 'img' property exists
   if(currentQuestion.hasOwnProperty("img")){
      const img = document.createElement("img");
      img.src = currentQuestion.img;
      questionText.appendChild(img);
   }

   // set options
   // get the length of options
   const optionLen = currentQuestion.options.length;
   // push options into availableOptions Array
   for(let i=0; i<optionLen; i++){
      availableOptions.push(i)
   }
   optionContainer.innerHTML = '';
   let animationDelay = 0.15;
   // create options in html
   for(let i=0; i<optionLen; i++){
      // random option
      const optonIndex = availableOptions[Math.floor(Math.random() * availableOptions.length)];
      // get the position of 'optonIndex' from the availableOptions Array
      const index2 =  availableOptions.indexOf(optonIndex);
      // remove the  'optonIndex' from the availableOptions Array , so that the option does not repeat
      availableOptions.splice(index2,1);
      const option = document.createElement("div");
      option.innerHTML = currentQuestion.options[optonIndex];
      option.id = optonIndex;
      option.style.animationDelay =animationDelay + 's';
      animationDelay = animationDelay + 0.15;
      option.className = "option";
      optionContainer.appendChild(option);
      option.setAttribute("onclick","getResult(this)");
   }
  console.log(availableQuestions)
  console.log(availableOptions)
   questionCounter++;
}

// get the result of current attempt question
function getResult(element){
    const id = parseInt(element.id);
    // get the answer by comparing the id of clicked option
    if(id === currentQuestion.answer){
       // set the green color to the correct option
       element.classList.add("correct");
       // add the indicator to correct mark
       updateAnswerIndicator("correct");
       correctAnswers++;
    }
    else{
       // set the red color to the incorrect option
       element.classList.add("wrong");
       // add the indicator to wrong mark
       updateAnswerIndicator("wrong");

       // if the answer is incorrect then show the correct option by adding green color the correct option
       const optionLen = optionContainer.children.length;
       for(let i=0; i<optionLen; i++){
          if(parseInt(optionContainer.children[i].id) === currentQuestion.answer){
             optionContainer.children[i].classList.add("correct");  		
          }
       }   
      
    }
  attempt++;
  unclickableOptions();
}

// make all the options unclickable once the user select a option (RESTRICT THE USER TO CHANGE THE OPTION AGAIN)
function unclickableOptions(){
   const optionLen = optionContainer.children.length;
   for(let i=0 ; i<optionLen; i++){
      optionContainer.children[i].classList.add("already-answered");
   }
}

function answersIndicator(){
     answersIndicatorContainer.innerHTML = '';
     const totalQuestion = questionLimit;
     for(let i=0; i<totalQuestion; i++){
          const indicator = document.createElement("div");
        answersIndicatorContainer.appendChild(indicator);
     }
}
function updateAnswerIndicator(markType){
    answersIndicatorContainer.children[questionCounter-1].classList.add(markType);
}

function next(){
  if(questionCounter === questionLimit){
       quizOver();
  }
  else{
      getNewQuestion();
  }
}

function quizOver(){
   // hide quiz Box
   questionsBox.classList.add("hide");
   // show result Box
   resultBox.classList.remove("hide");
   quizResult();
   saveResults();
}


// get the quiz Result
function quizResult(){
  resultBox.querySelector(".total-question").innerHTML = questionLimit;
  resultBox.querySelector(".total-attempt").innerHTML = attempt;
  resultBox.querySelector(".total-correct").innerHTML = correctAnswers;
  resultBox.querySelector(".total-wrong").innerHTML = attempt - correctAnswers;
  const percentage = (correctAnswers/questionLimit)*100;
  resultBox.querySelector(".percentage").innerHTML =percentage.toFixed(2) + "%";
  resultBox.querySelector(".total-score").innerHTML =correctAnswers +" / " + questionLimit;
  updateResults()
}

function resetQuiz(){
   questionCounter = 0;
   correctAnswers = 0;
   attempt = 0;
   availableQuestions = [];
}

function tryAgainQuiz(){
    // hide the resultBox
    resultBox.classList.add("hide");
    // show the questionsBox
    questionsBox.classList.remove("hide");
    resetQuiz();
    startQuiz();
}

function goToHome(){
   // hide result Box
   resultBox.classList.add("hide");
  prevResultBox.classList.add("hide");

   // show home box
   instructionBox.classList.remove("hide");
   resetQuiz();
}

function goToDashboard(){
  // hide result Box
  window.location.href = '/dashboard';
}

// #### STARTING POINT ####

function startQuiz(){
   
    // hide home box 
    instructionBox.classList.add("hide");
    prevResultBox.classList.add("hide")
    // show quiz Box
    questionsBox.classList.remove("hide");
   // first we will set all questions in availableQuestions Array
   setAvailableQuestions();
   // second we will call getNewQuestion(); function
   getNewQuestion();
   // to create indicator of answers
   answersIndicator();

}


window.onload = function (){
  instructionBox.querySelector(".total-question").innerHTML = questionLimit;
}



var server = "http://127.0.0.1:5000";
var results= { 'output': [questionLimit, 0,0,0]};


function updateResults(){
  results['output'] = [questionLimit, attempt, correctAnswers, attempt-correctAnswers];
}
        
function saveResults(){
        var appdir='/quiz';
        var send_msg = "Sending save request";
        var received_msg = "Results saved.";
        console.log(send_msg);
        $.ajax({
             type: "POST",
             url:server+appdir,
             data: JSON.stringify(results),
             dataType: 'json'
        }).done(function(data) { 
           console.log(data);
           console.log(received_msg);
        });
     }

function pastQuiz(){

  var prevAttempt = document.getElementById("pAttempt").innerHTML;
  var prevWrong = document.getElementById("pWrong").innerHTML;
  var prevCorrect = document.getElementById("pCorrect").innerHTML;
  var prevScore = document.getElementById("pScore").innerHTML;
  
  if (prevAttempt == 0){
     alert("You have not attemped the quiz yet, give it a go!")
  }
  else {
     
     alert("You have attemped the quiz!")
     instructionBox.classList.add("hide")
     prevResultBox.classList.remove("hide") 
     prevResultBox.querySelector(".total-question").innerHTML = questionLimit;     
     prevResultBox.querySelector(".total-attempt").innerHTML = prevAttempt;
     prevResultBox.querySelector(".total-correct").innerHTML = prevCorrect;
     prevResultBox.querySelector(".total-wrong").innerHTML = prevWrong;
     prevResultBox.querySelector(".total-score").innerHTML =prevScore *100 + "%";

  }
  
}
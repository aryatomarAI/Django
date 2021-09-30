var player1=prompt("Please Enter your Name Player1, Your chip color will be blue: ")
var player1Color='rgb(0, 48, 73)'
var player2=prompt("Please Enter your Name Player2, Your chip color will be red: ")
var player2Color="rgb(214, 40, 40)"
var table=$("table tr")



function reportWin(rowNum,colNum){
  console.log("You win starting at this row, col:");
  console.log(rowNum);
  console.log(colNum);
}


// Function for changing color
function changeColor(rowIndex,colIndex,color){
  return table.eq(rowIndex).find('td').eq(colIndex).find('input').css('background-color',color);

}


// Function report Back to current color of a button
function returnColor(rowIndex,colIndex){
  return table.eq(rowIndex).find('td').eq(colIndex).find('input').css("background-color");
}


// This function takes in the column index and returns the bottom row that is still gray
function checkBottom(colIndex){
  var colorReport=returnColor(5,colIndex);
  for (var row = 5; row >-1 ; row--) {
    colorReport=returnColor(row,colIndex);
    if (colorReport==='rgb(216, 243, 220)'){
      return row
    }
  }
}


// Check if the 4 input are of the same color
function colorMatch(one,two,three,four){
  if(one===two && one===three && one===four && one !='rgb(216, 243, 220)' && one !==undefined){
    return true;
  }
};


// Check if the horizontal Wins
function horizontalWinCheck(){
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
     if (colorMatch(returnColor(row,col),returnColor(row,col+1),returnColor(row,col+2),returnColor(row,col+3))) {
         console.log("Horizontal");
         console.log(reportWin(row,col))
         return true;
     }else{
       continue;
     }
    }
  }
}

// check if the vertical Wins
function verticalWinCheck(){
  for (var col = 0; col < 7; col++) {
      for (var row = 0; row <3 ; row++) {
        if (colorMatch(returnColor(row,col),returnColor(row+1,col),returnColor(row+2,col),returnColor(row+3,col))) {
            console.log("vertical");
            reportWin(row,col)
            return true;
        }else{
          continue;
        }
  }
}
}

// Check for the diagonal win
function diagonalWinCheck(){
  for(col=0;col<4;col++){
    for(row=0;row<6;row++){
      if (colorMatch(returnColor(row,col),returnColor(row+1,col+1),returnColor(row+2,col+2),returnColor(row+3,col+3))) {
          console.log("horizontal");
          reportWin(row,col)
          return true;
    }else if (colorMatch(returnColor(row,col),returnColor(row-1,col+1),returnColor(row-2,col+2),returnColor(row-3,col+3))) {
      console.log("horizontal");
      reportWin(row,col)
      return true;
    }else{
      continue;
    }
  }
}
}



function gameEnd(winner){
  $("h3").fadeOut('fast')
  $("h4").fadeOut("fast")
  $('h1').text(winner+" has won! Refresh your browser to play again!").css("fontSize", "50px")
  alert(winner+" has won,Please refresh the browser to start again")
}



var currentPlayer=1;
var cPlayerName=player1;
var cPlayerColor=player1Color;


$("h4").text(player1 + ": It's your turn, please pick a column to drop your blue chip.")


$(".chipboard input").on('click',function(){
  //find which column is clicked
  var col=$(this).closest('td').index();

  // find row to drop the chip
  var bottomRow=checkBottom(col);

  // drop the chip in the empty bottom Column
  changeColor(bottomRow,col,cPlayerColor);

  currentPlayer=currentPlayer* -1;

  if(currentPlayer===1){
    cPlayerName=player1;
    $("h4").text(cPlayerName + ": It's your turn, please pick a column to drop your blue chip.");
    cPlayerColor=player1Color;
  }else{
    cPlayerName=player2;
    $("h4").text(cPlayerName + ": It's your turn, please pick a column to drop your red chip.");
    cPlayerColor=player2Color;
  }

  // check for the win
  if(horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()){
    gameEnd(cPlayerName);
  }




});

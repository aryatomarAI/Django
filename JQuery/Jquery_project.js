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
function changeColor(rowIndex,colIndex){
  return table.eq(rowIndex).find('td').eq(colIndex).css('background-color',color);

}


// Function report Back to current color of a button
function returnColor(rowIndex,colIndex){
  return table.eq(rowIndex).find('td').eq(colIndex).css("background-color");
}


// This function takes in the column index and returns the bottom row that is still gray
function checkBottom(colIndex){
  var colorReport=returnColor(5,colIndex);
  for (var row = 5; row >-1 ; row--) {
    colorReport=returnColor(row,colIndex);
    if (colorReport==="rgb(216, 243, 220)"){
      return row
    }
  }
}


// Check if the 4 input are of the same color
function colorMatch(one,two,three,four){
  return (one===two && one===three && one===four && one !=="rgb(216, 243, 220)" && one !==undefined);
}


// Check if the horizontal Wins
function horizontalWinCheck(){
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
     if (colorMatch(returnColor(row,col),returnColor(row,col+1),returnColor(row,col+2),returnColor(row,col+3))) {
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
        if (colorMatch(returnColor(row,col),returnColor(row+1,col),returnColor(row+1,col),returnColor(row+1,col))) {
            return true;
        }else{
          continue;
        }
  }
}

console.log("Sleep In Problem")
function sleepIn(weekday,vacation){
  if (weekday=="sunday" || weekday=="saturday" || vacation=="yes"){
  console.log("True");
}else {
    console.log("False");
  }
}



function monkeyTrouble(aSmile, bSmile) {
    if (aSmile==true && bSmile==false || aSmile==false && bSmile==true) {
       console.log("false");
    } else {
      console.log("true");
    }
}


function stringTimes(str, n) {
    var j=1
    var k=str
    while (j<=n-1) {
    str=str+k
    j++
    }
    console.log(str);
}

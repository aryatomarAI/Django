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


function luckySum(a, b, c){
 if (a==13) {
   return 0
 }else if(b==13){
   return a
 }else if(c==13){
   return a+b
 }else{
  return a+b+c
}
}


function caught_speeding(speed, is_birthday){
   if (is_birthday==true){
   speed=speed-5
   }
   if (speed<= 60) {
     return 0
   } else if (speed>60 && speed<=80) {
     return 1
   }else if (speed>80){
     return 2
   }
}

function makeBricks(small, big, goal){

  quo=Math.floor(goal/5)
  rem=goal%5
  if(quo<=big && rem<=small){
    return true
  }else{
    return false
  }


}

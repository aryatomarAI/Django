var x=0;
while (x<5) {
console.log("x is currently: "+x)
console.log("x is currently less than 5, adding 1 to x")
x++
}
var y=0;
console.log("Now we are going to use Break to breakout of the loop")
while (y<10) {
console.log("y is currently: "+y+" but we will stop at 6 using break")
if(y===6){
  console.log("We have reached 6, Let's break out of this loop")
  break;
}
y++
}
console.log("  ")
console.log("  ")
console.log("Now we are going to find even numbers between 0 and 30 using JS")
var n=1;
while(n<30){
  if(n%2===0){
    console.log("Even number: "+n);
  }
 n++
}

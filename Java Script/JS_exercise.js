console.log("Printing Hello 5 times using while and for loop.");
console.log("Using While")
var x=0;
while(x<5){
console.log("Hello");
x++
}
console.log(" ")
console.log("Using For Loop");
for (var i = 0; i <5; i++) {
  console.log("Hello");
}
console.log("  ")
console.log("Using while loop to print out all the odd numbers between 0 and 25")
n=1
while (n<25) {
if (n%2===1) {
console.log(n);
}
n++
}
console.log(" ")
console.log("Using for loop to print out odd numbers between 0 and 25");
for (var i = 0; i < 25; i++) {
  if (i%2===1) {
   console.log(i);
  }
}

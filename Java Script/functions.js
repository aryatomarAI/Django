function addNum(num1,num2){
  console.log(num1 + num2);
}

addNum(2,3)

function helloName(name="Franky"){
  console.log("Hello " + name)
}
function formal(name="Sam",title="Sir"){
  return title + " " + name
}

var v="Global v variable"
var s="Global s variable"

function fun(s){
  console.log(v);
  s="Reassigning s inside the function"
  console.log(s);
}


fun();
console.log(s)

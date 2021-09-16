var hot=false;
var temp=40;
if (temp>=80) {
  hot=true;
  console.log("It's very Hot Outside")
}else if (temp<=80 && temp>=50) {
  console.log("It's Normal Temperature outside");
}else if(temp>=32 && temp<50){
  console.log("It's pretty cold outside");
}else if (temp>=0 && temp<=32) {
  console.log("It's very cold outside");
}

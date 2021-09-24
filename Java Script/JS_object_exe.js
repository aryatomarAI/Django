//Problem 1 Add a method which can length of the employees name to the console.

var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}
 employee.namelength=function(){
   return console.log(employee.name.length);

 }

 //Problem 2 Write program that will create an Alert in the browser of each of the object's values for the key value pairs
 var employee1 = {
   name: "John Smith",
   job: "Programmer",
   age: 31
 }

 function alert1(){
   text=""
  for (key in employee1 ) {
     text=text + key + " is " + employee1[key] +", "
   }
   return alert(text)
 }


 // problem 3 Add a method called lastName that prints out the employee's last name to the console.

 var employee2 = {
   name: "Arya Tomar",
   job: "Programmer",
   age: 25
 }
employee2.lastName=function(){
  var str1=employee2.name
  const myArr=str1.split(" ")
  return console.log(myArr[1]);
}

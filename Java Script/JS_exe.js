alert("Visitor Welcome to our Website!!")
var first=prompt("Please enter your first name:")
var second=prompt("Please enter your second name:")
var age=prompt("Please enter your age:")
var height=prompt("Please enter your height in cm:")
var pet=prompt("Enter your pet name:")
alert("Thank You for submitting all the details. Your details are safe with us. We will not share your details with any one else:")
if (first[0]===second[0] && age>20 && age<30 && height>170 && pet.slice(-1)==='y'){
  console.log("Welcome agent "+first + " " +second + " to our spy agency");
}
else {
  console.log("Welcome to our website");
}

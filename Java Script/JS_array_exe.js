var start=prompt("Would you like to start the roster web app? y/n")

var arr=[]
if (start=="y") {
   var choice="null"
   while (choice!=="quit") {
       choice=prompt("Please select an action: add, remove, display, or quit.")
       if (choice=="add") {
         var add1=prompt("What name would you like to add?")
         arr.push(add1)
       }else if (choice=="remove") {
         var value=prompt("What name would you like to remove?")
         arr= arr.filter(function(item){
             return item!==value
         })
       }else if (choice=="display") {
         alert(arr)
       }
   }
   alert("Thanks for using the Web App! Please refresh the page to start over.")
}else{
  alert("Thanks for using the Web App! Please refresh the page to start over.")
}

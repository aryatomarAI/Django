var headOne=document.querySelector("#one")
var headTwo=document.querySelector("#two")
var headThree=document.querySelector("#three")
headOne.addEventListener("mouseover",function(){
  headOne.textContent="You are Hovering over this text";
  headOne.style.color="Salmon";
})
headOne.addEventListener("mouseout",function(){
  headOne.textContent="Hover Over Me!"
  headOne.style.color="Black"
})
headTwo.addEventListener("click",function(){
  headTwo.textContent="You has clicked the text."
  headTwo.style.color="Blue"
})
headThree.addEventListener("dblclick",function(){
  headThree.textContent="BOOM!!!!BOOOM!!"
  headThree.style.color="Red"
})

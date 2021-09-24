var header=document.querySelector("h1")
header.style.color="salmon"

function randomColorSelector(){
var myColors=['#001219','#005F73','#0A9396','#94D2BD','#E9D8A6',"#EE9B00","#CA6702","#BB3E03","#AE2012","#9B2226"]
 return myColors[Math.floor(Math.random()*10)]
}

function changeHeaderColor(){
  colorInput = randomColorSelector()
  header.style.color = colorInput;
}
setInterval("changeHeaderColor()",500)

var restart=document.querySelector("#restart")
var cell=document.querySelectorAll("td")

// To remove all the
function reset(){
   for (var i = 0; i < cell.length; i++) {
     cell[i].textContent= '';
}
}

restart.addEventListener("click",reset)


function x(){
  if (this.textContent==="") {
      this.textContent="X";
  }else if(this.textContent==="X"){
    this.textContent="O";
  }else{
    this.textContent=""
  }
}


for (var i = 0; i < cell.length; i++) {
  cell[i].addEventListener("click",x)
}

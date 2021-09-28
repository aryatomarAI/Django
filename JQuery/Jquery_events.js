// JQuery Events
$('h1').click(function(){
  console.log("You have clicked on the heading!");
  alert("You have clicked on the heading!!")
})


$('li').dblclick(function(){
  console.log("You have clicked on the list item!");
  alert("You double clicked on the list item")
})


$('h1').click(function(){
  console.log("You have changed the heading text!");
  $(this).text("You have changed the text just by clicking on it")
})


// Key Press
$("input").eq(0).keypress(function(){
  $('h3').toggleClass("turnBlue")
})


// (event) event==13 is Enter
$('input').eq(0).keypress(function(event){
if (event.which===13) {
  $('h3').toggleClass("turnRed");

}
})

// On() method
$('h2').on("mouseenter",function(){
  $(this).css('color',"salmon")
})
$('h2').on("mouseout",function(){
  $(this).css('color',"black")
})


//Effects
$('input').eq(0).on('dblclick',function(){
  $(".container").fadeOut(4000);
})

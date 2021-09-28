// use $ sign to enable and grab attributes with jquery
var x= $("h1")

x.css('color','#E70D4F')
x.css('background','black')
x.css("border-radius","5px")

var listItems=$('li')
listItems.css('color','blue')
listItems.eq(0).css('color','orange')
listItems.eq(-1).css('color','red')


var h=$('h2')
h.text("This is a brand new text")
h.css('background','#E70D4F')
h.html("<strong>This is a new bold text.</strong>")

var inpu=$('input')
inpu.eq(1).attr("type","checkbox")
inpu.eq(0).val("New Value!")


// add and remove a class using jquery addClass and removeClass Method
var y=$("h3")
y.addClass("turnRed")
y.removeClass("turnRed")

// We can use toggle class instead of add and remove class
y.toggleClass('turnBlue')
y.toggleClass("turnBlue")

console.log("Defining a variable object carInfo");
var carInfo={make:"toyota",year:2006,model:"camery",color:"black"}
console.log("carInfo= "+carInfo)
console.dir(carInfo)
carInfo["make"]
carInfo["year"]+=1
for(key in carInfo){
  console.log(key)
}
for(key in carInfo){
  console.log(carInfo[key]);
}
console.log("Defining another object myO to show how versatile object is")
var myO={a:"hello",b:[1,2,3,4],c:{inside:["a","b"]}}
console.log("myO= "+myO);
console.dir(myO)
myO["b"][2]
myO["c"]["inside"][0]

var myObj={name:"Arya Tomar",
greet: function(){
  console.log("Hello "+this.name)
}}
myObj["name"]
myObj.greet()

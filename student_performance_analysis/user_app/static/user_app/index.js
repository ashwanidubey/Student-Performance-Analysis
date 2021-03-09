console.log("suny");
console.warn("good");
//alert("be honest");
var dd=new Date();
document.write(dd);

/*var myvar=setInterval(myTime,1000);
//setTimeout(function(){ alert("Hello"); }, 3000);
//setInterval(function(){ alert("Hello"); }, 3000);
//var myVar = setInterval(myTimer, 1000);
var s = new Date();
var tf = d.toLocaleTimeString();
function myTime() {
  var d = new Date();
  var t = d.toLocaleTimeString();
  document.getElementById("mytimer").innerHTML = t-tf;
}*/
//

var countDownDate = new Date().getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = 30*1000-( now-countDownDate) ;

  // Time calculations for days, hours, minutes and seconds
  //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  //var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("mytimer").innerHTML = minutes + "m " + seconds + "s ";

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("mytimer").innerHTML = "EXPIRED";
    alert("time over");
  }
}, 1000)

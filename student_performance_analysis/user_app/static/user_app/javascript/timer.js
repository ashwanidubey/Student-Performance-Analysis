

//alert(diff)
  //x.innerHTML="bad"
function calltimer()
{
   var x = document.getElementById("difference");
   var year=x.getAttribute("year")
   var month=x.getAttribute("month")
   var day=x.getAttribute("day")
   var hour=x.getAttribute("hour")
   var minute=x.getAttribute("minute")
   var second=x.getAttribute("second")
   var fix=new Date(year,month,day,hour,minute,second)
   var countDownDate=fix.getTime()
   var no = new Date()
   var now=no.getTime();
   var distance = countDownDate - now;

   var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
   var seconds = Math.floor((distance % (1000 * 60)) / 1000);
   //x.innerHTML =ety+"/"+etm+"/"+eth+"/"+etmin+"/"+ets;
  // x.innerHTML="good"
  if(minutes==0 && seconds==0)
  {
    //alert("bnd kro bhot hua")
    var y = document.getElementById("mr_hidden");
    var z = document.getElementById("mr_shown");
    z.style.display= "none";
    y.style.display= "block";

  }
  x.innerHTML="min: 0"+minutes+" sec: "+seconds
}
 setInterval(calltimer,1000);

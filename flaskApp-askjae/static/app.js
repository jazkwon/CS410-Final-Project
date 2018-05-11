function sayHello(){
  alert("hello world!")
}

function getTabs(event, type){
  //var tabcontent, tablinks;
  var curr = document.getElementById(type);

  if (curr.style.display === "none"){
    curr.style.display = "block";
  }
  else{
    curr.style.display = "none";
  }

}

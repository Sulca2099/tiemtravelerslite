function startsessionstorage(){
  sessionStorage.setItem("health",100);
}
function justgo(urlfor){//function to go to another room
  window.location.href=urlfor;//change the url to the room
}
function justgo(urlfor){//function to go to another room
  sessionStorage.clear();
  startsessionstorage();
  window.location.href=urlfor;//change the url to the room
}
function gowith(){}//function for going to room, but it requires something to execute
function justtalk(){}//function to make a popup for the converstions
function claim(item,amount,location){
  if(sessionStorage.getItem(location)==null){
    sessionStorage.setItem(item,sessionStorage.getItem(item)+amount);
    sessionStorage.getItem(location)="true";
  } else{
    alert("you took this item already, find something else...");
  }
}

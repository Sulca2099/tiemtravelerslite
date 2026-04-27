function startsessionstorage(){
  sessionStorage.setItem("health",100);
}
window.onload= function(){
  document.getElementById('stats').innerText=`health ${sessionStorage.getItem("health")}`;
}

function resetgo(urlfor){//function to go to another room
  sessionStorage.clear();
  startsessionstorage();
  window.location.href=urlfor;//change the url to the room
}
function randomgo(locations){
  window.location.href=locations[(Math.floor(Math.random()*locations.length)/1)];
}
function gowith(page,stats){
  if(stats[1]==sessionStorage.getItem(stats[0])){
    window.location.href=page;
  } else{
    alert(`you don't have enough ${stats[0]}`);
  }
}//function for going to room, but it requires something to execute
function justtalk(){}//function to make a popup for the converstions
function claim(item,amount,location){
  if(sessionStorage.getItem(location)==null){
    sessionStorage.setItem(item,sessionStorage.getItem(item)+amount);
    sessionStorage.setItem(location,"true");
  } else{
    alert("you took this item already, find something else...");
  }
}
function unclaim(item,amount,location){
  if(sessionStorage.getItem(location)==null){
    sessionStorage.setItem(item,sessionStorage.getItem(item)-amount);
    sessionStorage.setItem(location,"true");
    if(sessionStorage.getItem("health")<=0){
      window.location.href="dead.html";
    }
  } 
}
function justgo(urlfor){//function to go to another room
  sessionStorage.setItem(item,sessionStorage.getItem("health")+.1);
  window.location.href=urlfor;//change the url to the room
  
}

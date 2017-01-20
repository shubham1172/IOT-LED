window.onload = function(){
var red = document.getElementById('r');
var yellow = document.getElementById('y');
var green = document.getElementById('g');

function reqListener(){
	console.log(this.responseText);
}

function request(code){
	var req = new XMLHttpRequest();
	req.addEventListener("load", reqListener);
	req.open("GET", "glow/"+code);
	req.send();
}

red.onclick = function(){
	request("R");
}
yellow.onclick = function(){
	request("Y");
}
green.onclick = function(){
	request("G");
}
}

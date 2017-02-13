var change_class = function(id, class_name){
	var doc = document.getElementById(id)
	doc.className = class_name
}

document.getElementById("hamburger").onclick = function(){
	if (document.getElementById("navbar").className == "inactive"){
	change_class("navbar", "nav")
	}
	else{
		change_class("navbar", "inactive")
	}
}
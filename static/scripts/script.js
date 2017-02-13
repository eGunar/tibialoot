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

screensize = $(window).width();
if (screensize >= 1000){
	change_class("navbar", "nav")
}

$(window).resize(function () {
	screensize = $(window).width();
	if (screensize >= 1000){
		change_class("navbar", "nav")
	}
});


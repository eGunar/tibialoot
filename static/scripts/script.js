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

var togglebutton = function(id, desired_class){
	if (document.getElementById(id).className == "inactive"){
	change_class(id, desired_class)
	}
	else{
		change_class(id, "inactive")
		change_class(this.id, 'inactive')
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


function deselect(e) {
  $('.pop').slideFadeToggle(function() {
    e.removeClass('pressed');
  });    
}

$(function() {
  $('#custom_prices').on('click', function() {
    if($(this).hasClass('pressed')) {
      deselect($(this));               
    } else {
      $(this).addClass('pressed');
      $('.pop').slideFadeToggle();
    }
    return false;
  });

  $('.close').on('click', function() {
    deselect($('#custom_prices'));
    return false;
  });
});

$.fn.slideFadeToggle = function(easing, callback) {
  return this.animate({ opacity: 'toggle', height: 'toggle' }, 'fast', easing, callback);
};

document.getElementById('Alesar').onclick = function(){
	togglebutton('Alesarlist', 'show')
}
document.getElementById('Rashid').onclick = function(){
	togglebutton('Rashidlist', 'show')
}
document.getElementById('Nahbob').onclick = function(){
	togglebutton('Nahboblist', 'show')
}
document.getElementById('Tesha').onclick = function(){
	togglebutton('Teshalist', 'show')
}
document.getElementById('Haroun').onclick = function(){
	togglebutton('Harounlist', 'show')
}
document.getElementById('Yaman').onclick = function(){
	togglebutton('Yamanlist', 'show')
}
document.getElementById('Yasir').onclick = function(){
	togglebutton('Yasirlist', 'show')
}
document.getElementById('Lailene').onclick = function(){
	togglebutton('Lailenelist', 'show')
}
document.getElementById('Telas').onclick = function(){
	togglebutton('Telaslist', 'show')
}
document.getElementById('Tamoril').onclick = function(){
	togglebutton('Tamorillist', 'show')
}
document.getElementById('Alexander').onclick = function(){
	togglebutton('Alexanderlist', 'show')
}
document.getElementById('Esrik').onclick = function(){
	togglebutton('Esriklist', 'show')
}
document.getElementById('Bone_master').onclick = function(){
	togglebutton('Bone_masterlist', 'show')
}
document.getElementById('Player_items').onclick = function(){
	togglebutton('Player_itemslist', 'show')
}
document.getElementById('Gold').onclick = function(){
	togglebutton('Goldlist', 'show')
}
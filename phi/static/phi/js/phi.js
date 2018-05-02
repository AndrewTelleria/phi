// Sticky navbar
window.onscroll = function() {stickyNavbar()};
var navbar = document.getElementById("myNavbar");
var sticky = navbar.offsetTop + 650;

function stickyNavbar() {
	if (window.pageYOffset + 650 >= sticky) {
		navbar.classList.add("sticky");
	} else {
		navbar.classList.remove("sticky");
	}
}
// End sticky navbar

// Menu icon for small screen devices

function menuIcon(x) {
	x.classList.toggle("change");
}

function responsiveMenu() {
	var x = document.getElementById("responsive-menu");
	var y = document.getElementById("myNavbar");

	x.classList.toggle("disappear");
	y.style.height = "150px";
}
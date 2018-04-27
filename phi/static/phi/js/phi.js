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
var flky = new Flickity( '.main-carousel', {
	accessibility: true,
	autoPlay: true,
	fullscreen: true,
	cellAlign: 'center',
	draggable: '>1',
	lazyLoad: true
});

// Menu icon for small screen devices

function menuIcon(x) {
	x.classList.toggle("change");
}

function responsiveMenu(x) {
	var menuClass = document.getElementById("responsive-menu");
	console.log(menuClass)
	menuClass.classList.toggle("menu-on");
}


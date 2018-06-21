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

function responsiveMenu() {
	var x = document.getElementById("responsive-menu");
	var y = document.getElementById("myNavbar");
	console.log(x);

    if (x.className === "responsive") {
        x.className += " menu-on";
    } else {
        x.className = "topnav";
    }
}
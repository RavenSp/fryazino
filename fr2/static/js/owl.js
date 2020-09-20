$(document).ready(function(){

  $(".owl-carousel").owlCarousel({
  	items:4,
  	loop:true,
  	autoplay:true,
  	margin: 15,
  	responsive:{
        0:{
            items:1,
            nav:false
        },
        460:{
        	items:2,
            nav:false
        },
        800: {
        	items:3,
            nav:false
        },

        1025: {
        	items:4,
            nav:false
        },
        1250: {
        	items:6,
            nav:false
        }
    }
  });
});
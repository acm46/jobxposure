$(document).ready(function(){
	var scrollorama = $.scrollorama({
		blocks: '.scrollblock'
	});

	scrollorama
		.animate('#jobxposure', {delay:0, duration:700, property:'opacity', start:0})
		.animate('#upload', { delay:200, duration:800, property:'opacity', start:0});

});
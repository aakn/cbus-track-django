$(function(){

	// Adds some data to the table
	window.update_table = function(lat,lon,time,moved,speed) {
		$("#lat").html(lat);
		$("#lon").html(lon);
		var date = Date.parse(time);
		time = date.toString("MMMM d, yyyy - hh:mm:ss tt");
		time = time.replace(/ - 00:/, " - 12:");
		$("#time").html(time);
		$("#move").html(moved);
		$("#speed").html(speed+" KMPH");
	}

});

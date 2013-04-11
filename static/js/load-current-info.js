$(function(){

		// Just a placeholder function
	window.append_table = function() {}

	// Adds some data to the table
	window.update_table = function(lat,lon,time,moved,speed) {
		update_address(lat,lon);
		$("#lat").html(lat);
		$("#lon").html(lon);
		var date = Date.parse(time);
		time = date.toString("MMMM d, yyyy - hh:mm:ss tt");
		time = time.replace(/ - 00:/, " - 12:");
		$("#time").html(time);
		$("#move").html(moved);
		$("#speed").html(speed+" KMPH");
	}

	// Updates the address by getting doing a reverse geolocation
	function update_address(lat,lon) {
		$.getJSON("/maps/get_address/"+lat+"/"+lon+"/", function(result){
			console.log(result);
			$("#address").html(result["address"]);
		});
	}

	var socket = new SocketBox('apikey');
	socket.subscribe('track-channel');
	socket.bind('bus-moved', function(data) {
		console.log(data);
		console.log("BUS ID="+data.bus_id);
		console.log("Latitude="+data.lat);
		console.log("Longitude="+data.lon);
		var address = JSON.parse(data.address);
		console.log("Address="+address.address);
		console.log("Speed="+data.speed);
		console.log("Time="+data.time);
	})
});

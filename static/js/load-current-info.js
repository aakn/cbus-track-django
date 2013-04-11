$(function(){

	// Adds to the All buses table
	window.append_table = function(id, number, address, time) {
		$('.all-stats-body').append("<tr id='bus"+id+"'><td><button style='width:100%;' class='btn btn-inverse bus-route-selector' onclick='update_route("+id+");'>"+number+"</button></td><td id='all-stats-table-address" + id + "'>"+address+"</td><td id='all-stats-table-time" + id + "'>"+time+"</td></tr>");			
	}

	// Updates the all buses table
	window.update_all_buses_stats = function(id, address, time) {
		$("#all-stats-table-address"+id).html(address);
		$("#all-stats-table-time"+id).html(time);
	}
	// Adds some data to the table
	window.update_table = function(lat,lon,time,moved,speed,address) {
		if(address == '')
			update_address(lat,lon);
		else
			$("#address").html(address);
		$("#lat").html(lat);
		$("#lon").html(lon);
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
	});

	// Converts time to appropriate format.
	window.parse_time = function(time) {
		var date = Date.parse(time);
		time = date.toString("MMMM d, yyyy - hh:mm:ss tt");
		time = time.replace(/ - 00:/, " - 12:"); 	
		return time;
	}
});

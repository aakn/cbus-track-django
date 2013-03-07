$(function(){

	var bus_id = 1;

	var lat,lon;
	var map,marker,currentCenter,currentPath;

	var coord_array = new Array();

	var i=0;
	var hidden = true;

	/* PUSHER CODE */
	var pusher = new Pusher('38c410e14df2239c04ab');
	var channel = pusher.subscribe('track-channel');
	channel.bind('bus-moved', function(data) {
		if(data.bus_id == bus_id)
			push_data(data);	// Checks if the data is for the same bus route.
	});
	/* PUSHER CODE END */

	// Initialization Code for Google Maps
	function initialize()
	{
		currentCenter = coord_array[i-1];
		var mapProp = {
			center: currentCenter,
			zoom:15,
			mapTypeId:google.maps.MapTypeId.ROADMAP
		};
		map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

		marker=new google.maps.Marker({
			position: currentCenter,
			animation:google.maps.Animation.BOUNCE
		});
		marker.setMap(map);

		currentPath=new google.maps.Polyline({
			path:coord_array,
			strokeColor:"#0000FF",
			strokeOpacity:0.8,
			strokeWeight:2
		});

		currentPath.setMap(map);
		done_loading();
	}
	function setMarker(pos) {
		currentPath.setPath(coord_array);
		map.setCenter(pos);
		marker.setPosition(pos);
	}
	
	$.ajax({
		async: false,
		dataType: "json",
		url: "/ajax/last_trip/"+bus_id,
		success: function(data) {
			console.log("Data from the Previous coordinates...");

			data = data.reverse();
			console.log(data); 
			var speed, time, lat, lon;
			$.each(data, function(key,value) {
				var pos = new google.maps.LatLng(value.lat,value.lon);
				coord_array[i++] = pos;

				var data=value;

				lat = data.lat;
				lon = data.lon;
				speed = data.speed;
				time = data.time;
			});	
			update_table(lat,lon,time,"Last Trip",speed);
			update_address(lat,lon);
			console.log(coord_array); 
		}
	});

	console.log("after the synchronous ajax call...");
	google.maps.event.addDomListener(window, 'load', initialize);
	
	// Called after the maps is loaded...
	// Shows the table, and hides the loading bar.
	function done_loading() {
		if(hidden) {
			$("#loading-bar").hide();
			$(".stats-table").show();
			hidden = false;

		}
	}


	// This is called whenever a new value enters the database.
	function push_data(data) {
		console.log(data);

		var oldlat = lat;
		var oldlon = lon;

		lat = data.lat;
		lon = data.lon;
		speed = data.speed;
		time = data.time;
		

		if( lat == oldlat && lon == oldlon ) 
			update_table(lat,lon,time,"Stationary",speed);
		else {
			var pos = new google.maps.LatLng(lat,lon);
			coord_array[i] = pos;
			setMarker(pos);
			i++;
			update_table(lat,lon,time,"Moving",speed);
			update_address(lat,lon);
		}
	}	

	// Updates the address by getting doing a reverse geolocation
	function update_address(lat,lon) {
		$.getJSON("/geocode/"+lat+"/"+lon+"/", function(result){
			console.log(result);
			$("#address").html(result["address"]);
		});
	}

	// Adds some data to the table
	function update_table(lat,lon,time,moved,speed) {
		$("#lat").html(lat);
		$("#lon").html(lon);
		$("#time").html(time);
		$("#move").html(moved);
		$("#speed").html(speed+" KMPH");
	}

});

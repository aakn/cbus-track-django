$(function(){

	var bus_id = 0;
	var bus_number;
	var lat,lon;
	var map,marker,currentCenter,currentPath;

	var coord_array = new Array();
	var msg_array = new Array();
	var marker = new Array();

	var buses_list = new Array();

	var i=0;
	var hidden = true;

	$(".progress-ring").show();

	/* PUSHER CODE */
	// var pusher = new Pusher('38c410e14df2239c04ab');
	// var channel = pusher.subscribe('track-channel');
	// channel.bind('bus-moved', function(data) {
	// 	//if(data.bus_id == bus_id)
	// 		push_data(data);	// Checks if the data is for the same bus route.
	// });
	/* PUSHER CODE END */

	/* SOCKETBOX CODE */
	var socket = new SocketBox('apikey');
	socket.subscribe('track-channel');
	socket.bind('bus-moved', function(data) {
		push_data(data);
	});
	/* SOCKETBOX CODE END */

	// Initialization Code for Google Maps
	function initialize()
	{
		if(bus_id==0)
		{
			currentCenter = coord_array[i-1];
			var mapProp = {
				center: currentCenter,
				zoom:11,
				zoomControl: true,
				mapTypeId:google.maps.MapTypeId.ROADMAP
			};
			map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
			for(var ctr=0;ctr<i;ctr++) {
				marker[ctr]=new google.maps.Marker({
					position: coord_array[ctr],
					title : msg_array[ctr],
					icon:'/static/img/bus_position_marker.png',
				});
				marker[ctr].setMap(map);	
			}
		}
		else {
			currentCenter = coord_array[i-1];
			var mapProp = {
				center: currentCenter,
				zoom:15,
				mapTypeId:google.maps.MapTypeId.ROADMAP
			};
			map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

			marker=new google.maps.Marker({
				position: currentCenter,
				icon:'/static/img/bus_position_marker.png', 
				//animation:google.maps.Animation.BOUNCE
			});
			marker.setMap(map);

			currentPath=new google.maps.Polyline({
				path:coord_array,
				strokeColor:"#0000FF",
				strokeOpacity:0.8,
				strokeWeight:2
			});

			currentPath.setMap(map);

		}
		done_loading();


	}
	function setMarker(pos) {
		currentPath.setPath(coord_array);
		map.setCenter(pos);
		marker.setPosition(pos);
	}
	
	
	function get_some_default_values() {
		// Fills the table during the first run.
		// Gets around 50 last values from the table.
		if(bus_id==0)
		{
			$(".page-header-all-stats").html("<h2>Current State Of All Buses </h2>");

			$.ajax({
				async: false,
				dataType: "json",
				url: "/ajax/buses_status",
				success: function(data) 
				{
					console.log("Status of all buses...");

					console.log(data); 

					$(".stats-table-body").html("");
					coord_array = [];
					msg_array = [];
					i=0;

					$.each(data, function(key,value) {
						
						lat = value.lat;
						lon = value.lon;
						speed = value.speed;
						time = value.time;
						address_json_string = value.address;
						address_json = JSON.parse(address_json_string);
						address = address_json.address;

						current_bus_id = value.id;
						current_bus_number = value.number;

						buses_list.push( {
							id: current_bus_id,
							number: current_bus_number,
						});

						time = parse_time(time);

						append_table(current_bus_id, current_bus_number, address, time);

						var pos = new google.maps.LatLng(lat,lon);
						msg_array[i] = "BUS "+value.number+" was last updated on "+time;
						coord_array[i++] = pos;
						

					});	

					console.log(coord_array); 
				}
			});
		}	
		else {
			
			$.each(buses_list, function(key,val) {
				if(val.id==bus_id) {
					bus_number=val.number;
					$(".page-header-stats").html("<h2>Current State - "+bus_number+" </h2>");
				}
			});
			$.ajax({
				async: false,
				dataType: "json",
				url: "/ajax/last_trip/"+bus_id,
				success: function(data) {
					console.log("Data from the Previous coordinates...");

					data = data.reverse();
					console.log(data); 

					coord_array = [];
					i=0;

					$.each(data, function(key,value) {
						var pos = new google.maps.LatLng(value.lat,value.lon);
						coord_array[i++] = pos;


						var data=value;

						lat = data.lat;
						lon = data.lon;
						speed = data.speed;
						time = data.time;

					});	
					time = parse_time(time);
					update_table(lat,lon,time,"Last Trip",speed,'');
					console.log(coord_array); 
				}
			});
		}
	}

	get_some_default_values();
	console.log("after the synchronous  ajax call...");
	google.maps.event.addDomListener(window, 'load', initialize);

	// Called after the maps is loaded...
	// Shows the table, and hides the loading bar.
	function done_loading() {
		if(hidden) {
			$(".bus-details").show();
			$(".progress-ring").hide();
            $(".progress-ring").addClass("hidden");
			hidden = false;
		}
		$('.bus-route-selector').removeAttr('disabled');
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

		time = parse_time(time);

		current_bus_id = data.bus_id;

		address_json_string = data.address;
		address_json = JSON.parse(address_json_string);
		address = address_json.address;
		

		if(bus_id==0) {

			update_all_buses_stats(current_bus_id, address, time);
			
			if( lat != oldlat || lon != oldlon ) {
				var newLatLng = new google.maps.LatLng(lat, lon);
				marker[current_bus_id-1].setPosition(newLatLng);
				
			}
		}
		else if(data.bus_id==bus_id) {
			if( lat == oldlat && lon == oldlon ) 
				update_table(lat,lon,time,"Not Moved",speed,address);
			else {
				var pos = new google.maps.LatLng(lat,lon);
				coord_array[i] = pos;
				setMarker(pos);
				i++;
				update_table(lat,lon,time,"Moved",speed,address);
			}

		}
	}	

	

	window.update_route = function(new_id) {
		$(".progress-ring").show();
		hidden=true;

		bus_id = new_id;
		if(bus_id==0) {
			$('.stats').hide();
			$('.all-stats').show();			
			$('.all-stats-body').html("");

		}
		else {
			$('.stats').show();
			$('.all-stats').hide();	
			$(".stats-table-body").html("");

		}
		get_some_default_values();
		//google.maps.event.addDomListener(window, 'load', initialize);
		initialize();
	}
	$('.bus-route-selector').click(function(){
		$(this).attr('disabled', 'disabled');
	});
});

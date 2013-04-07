$(function(){

	var bus_id = 0;
	var bus_number;
	var lat,lon;
	var map,marker,currentCenter,currentPath;

	var coord_array = new Array();
	var msg_array = new Array();

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
		if(bus_id==0)
		{
			currentCenter = coord_array[i-2];
			var mapProp = {
				center: currentCenter,
				zoom:10,
				zoomControl: true,
				mapTypeId:google.maps.MapTypeId.ROADMAP
			};
			map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
			for(var ctr=0;ctr<i;ctr++)
			{
				marker=new google.maps.Marker({
				position: coord_array[ctr],
				//animation:google.maps.Animation.BOUNCE,
				title : msg_array[ctr]
			});
			marker.setMap(map);	
			}
			

			/*currentPath=new google.maps.Polyline({
				path:coord_array,
				strokeColor:"#0000FF",
				strokeOpacity:0.8,
				strokeWeight:2
			});

			currentPath.setMap(map);*/
			done_loading();

		}
		else
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

	}
	function setMarker(pos) {
		currentPath.setPath(coord_array);
		map.setCenter(pos);
		marker.setPosition(pos);
	}
	
	
	function get_some_default_values() {
		// Fills the table during the first run.
		//Gets around 50 last values from the table.
		if(bus_id==0)
		{
			$.ajax({
			async: false,
			dataType: "json",
			url: "/ajax/buses_status",
			success: function(data) 
			{
				console.log("Status of all buses...");

				//data = data.reverse();
				console.log(data); 

				$(".stats-table-body").html("");
				coord_array = [];
				msg_array = [];
				i=0;

				$.each(data, function(key,value)
				 {
					temp=JSON.parse(value.status);
					data=temp[0];
					//alert("key="+key+"value="+temp[0].lat)
					lat = data.lat;
					lon = data.lon;
					speed = data.speed;
					time = data.time;
		
					var pos = new google.maps.LatLng(lat,lon);
					msg_array[i] = "BUS "+value.number+" was Last updated on "+time;
					coord_array[i++] = pos;
					//append_table(lat,lon,time,"last-trip",speed);

				});	
				//update_table(lat,lon,time,"last-trip",speed);
				console.log(coord_array); 
			}
		});
		}	
		else
		{
			alert("BUS ID="+bus_id);
			$.ajaxSetup({
				async: false
			});
			$.getJSON('/ajax/list_of_routes', function(data) {
		 
			  $.each(data, function(key, val) {
			  if(val.id==bus_id)
			  	bus_number=val.route_number;
			  });
			});
			$.ajaxSetup({
				async: true
			});
			//alert("BUS NUMBER"+bus_number);
			$.ajax({
			async: false,
			dataType: "json",
			url: "/ajax/last_trip/"+bus_id,
			success: function(data) {
				console.log("Data from the Previous coordinates...");

				data = data.reverse();
				console.log(data); 

				$(".stats-table-body").html("");
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

					append_table(lat,lon,time,"last-trip",speed);

				});	
				update_table(lat,lon,time,"last-trip",speed);
				console.log(coord_array); 
			}
		});
			alert(bus_number);
			$("#busnum").html(bus_number);
		}
	}

	get_some_default_values();
	console.log("after the synchronous  ajax call...");
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
	// 
	function push_data(data) {
		console.log(data);

		var oldlat = lat;
		var oldlon = lon;

		lat = data.lat;
		lon = data.lon;
		speed = data.speed;
		time = data.time;
		

		if( lat == oldlat && lon == oldlon ) 
			update_table(lat,lon,time,"not-moved",speed);
		else {
			var pos = new google.maps.LatLng(lat,lon);
			coord_array[i] = pos;
			setMarker(pos);
			i++;
			update_table(lat,lon,time,"moved",speed);
		}
	}	

	window.update_route = function(new_id) {
		bus_id = new_id;
		get_some_default_values();
		//google.maps.event.addDomListener(window, 'load', initialize);
		initialize();
	}

});

function show_trip()
	{

	var bus_id = 1;
	var date="2013-04-17";
	var morn_even=0;
	var lat,lon;
	var map,marker,currentCenter,currentPath;

	var coord_array = new Array();

	var i=0;
	var hidden = true;
	
	$(".progress-ring").show();
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
			animation:google.maps.Animation.BOUNCE,
			icon:'/static/img/bus_position_marker.png',
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
	
	
	function get_some_default_values() {
		// Fills the table during the first run.
		//Gets around 50 last values from the table.
		$.ajax({
			async: false,
			dataType: "json",
			url: "/ajax/trip/"+bus_id+"/"+date+"/"+morn_even,
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
	}
	
		var date=document.getElementById("tripdate");
		alert(date.value);
		/*get_some_default_values();
		console.log("after the synchronous ajax call...");
		google.maps.event.addDomListener(window, 'load', initialize);*/
	
	
	// Called after the maps is loaded...
	// Shows the table, and hides the loading bar.
	function done_loading() {
		if(hidden) {
			$(".progress-ring").hide();
			$(".stats-table").show();
			hidden = false;

		}
	}
}

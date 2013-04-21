function show_trip()
	{

	var bus_id;
	var date;
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
			url: "/ajax/trip/"+bus_id+"/"+date.value+"/"+morn_even,
			success: function(data) {
				console.log("Data from the Previous coordinates...");

				data = data.reverse();
				console.log(data); 

				$(".stats-table-body").html("");
				coord_array = [];
				i=0;
				var dist=0;
				var lastlat,lastlon;
				$.each(data, function(key,value) {
					var pos = new google.maps.LatLng(value.lat,value.lon);
					coord_array[i++] = pos;
					if(i==0)
					{
						lastlat=lat;
						latlon=lon;
						dist=0;
					}
					else
					{
						dist=dist+computedisplacement(lat,lon,lastlat,lastlon);
						lastlat=lat;
						lastlon=lon;
					}
					console.log("coord="+pos);
					var data=value;

					lat = data.lat;
					lon = data.lon;
					speed = data.speed;
					time = data.time;

					append_table(lat,lon,time,"last-trip",speed);

				});	
				update_table(lat,lon,time,"last-trip",speed);
				console.log(coord_array); 
				console.log("distance="+dist);
			}
		});
	}
	
		date=document.getElementById("tripdate");
		//alert(date.value);
		bus_id=document.getElementById("bus").value;
		morn_even=document.getElementById("time").value;
		//alert("busid="+morn_even);
		get_some_default_values();
			console.log("after the synchronous ajax call...");
		//google.maps.event.addDomListener(window, 'load', initialize);
		initialize();
	
	// Called after the maps is loaded...
	// Shows the table, and hides the loading bar.

	function done_loading() {
		if(hidden) {
			$(".progress-ring").hide();
			$(".stats-table").show();
			hidden = false;

		}
	}
	//displacement function for co ordinates
	function computedisplacement(lat1,lon1,lat2,lon2) {
		var theta=lon1-lon2;
		var distance= Math.sin(deg2rad(lat1)) * Math.sin(deg2rad(lat2)) + Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * Math.cos(deg2rad(theta));
		dist = Math.acos(dist);
		dist = rad2deg(dist);
		dist = dist * 60 * 1.1515;
		dist = dist * 1.609344;
		return dist;
	}
	function deg2rad(deg) {
		return (deg * Math.PI / 180.0);
	}
	function rad2deg(rad) {
		return (rad * 180.0 / Math.PI);
	}
}

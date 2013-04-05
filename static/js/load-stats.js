$(function(){

	// Adds some data to the table
	window.update_table = function(lat,lon,time,moved,speed) {
		var mv = "<p style='color: red;'>Not Moved</p>";

		if(moved == "moved") 
			mv = "<p style='color: green;'>Moved</p>";
		else if(moved == "last-trip") 
			mv = "<p style='color: orange;'>Last trip</p>";


		var to_append = "<tr><td>"+lat+"</td><td>"+lon+"</td><td>"+time+"</td><td>"+speed+"</td><td>"+mv+"</td></tr>";

		$(".stats-table-body").html(to_append+$(".stats-table-body").html());
	}
});

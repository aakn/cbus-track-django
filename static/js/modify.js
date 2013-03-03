$(function() {

	var result;

	$(".edit-btn").click(function() {
		var id = this.id;
		$.post("../php/get-item.php",
		{ 
			itemid : id
		},
		function(data,status) {
			//console.log(data);
			result = JSON.parse(data); 
			console.log(result);

			$.each(result, function(key,value) {
				$("#"+key).val(value);
				//console.log(key+" "+value);
			});
		});

		//$('#edit-modal').modal();
	});
	$(".delete-btn").click(function() {
		var id = this.id;
		console.log(id);
		$.post("../php/delete.php",
		{ 
			itemid : id
		},
		function(data,status) {
			//console.log(data);
			if(data=="done") {

			}
		});
	});
	$("#save-changes-btn").click(function () {
		var items = new Object();
		var i=0;
		$.each(result, function(key,value) {
			items[key] = $("#"+key).val();
			//console.log(key+" "+value);
		});
		//console.log(items);

		$.post("../php/update-item.php", items,
		function(data,status) {
			$("#edit-modal").modal('hide');
			console.log(data);
				
		});


	});
});
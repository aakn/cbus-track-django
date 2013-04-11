/*!
 * SocketBox JavaScript Library v1.12.7
 * http://insigniadevs.com/
 *
 * Copyright 2013, SocketBox
 * Released under the MIT licence.
 */
;(function(){  
	

	window.SocketBox = function (apikey) {
		
		var host = 'http://50.62.76.127:4000';

		this.apikey = apikey;
		this.socket = io.connect(host);

		this.channel = null;

		var self = this;

		this.socket.on('ack', function (data) {
			SocketBox.log(data.status);
		});

		function log(data) {
			console.log("SocketBox : " + data );
		};

	};


	window.SocketBox.log = function(data) {
		console.log("SocketBox : " + data );
	};

	SocketBox.prototype = {
		bind: function(event_name, callback) {
			
			this.socket.on(this.channel, function(socket_data) {
				SocketBox.log("Event Received : " + JSON.stringify(socket_data));

				// If both channel name and event name match
				if(this.channel == socket_data.channel && socket_data.event == event_name) {
					json_data = JSON.parse(socket_data.data)
					callback(json_data);
				}
			});

			return this;
		},

		subscribe: function(channel_name) {
			this.channel = channel_name;
		},

		trigger: function(event_name, data) {
			SocketBox.log("Trigger yet to be added");
		},
	};

}).call(this);

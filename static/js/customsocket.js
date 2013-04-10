  var socket = io.connect('http://50.62.76.127:3000');
  socket.on('cbustrack-busmoved', function (data) {

    data=data.replace(/\'/g,"\"");
    console.log("RECEIVED DATA = "+data);
    data=JSON.parse(data);
    console.log("BUS ID="+data.bus_id);
    console.log("Latitude="+data.lat);
    console.log("Longitude="+data.lon);
    console.log("Address="+data.address.address);
    console.log("Speed="+data.speed);
    console.log("Time="+data.time);	   
    
  });

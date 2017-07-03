var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var exec = require('child_process').exec;

var pid = ""
var fakepid = ""

app.get('/mothership', function(req,res){
    res.sendFile(__dirname + ('/control.html'));
})
io.on('connection', function(socket){
    console.log("You have connected to the mothership");
    socket.on('startProcess', function(msg){
        var child2 = exec("python2.7 Belle.py", function(err, stdout, stderr){
            console.log("stdout: " + stdout);
            if(err !== null){
                console.log("stderr: " + stderr);
                console.log("exec err: " + err);
            }
        });
        var child = exec("ps -ef | grep '[B]elle.py' | awk '{print $2}'", function(err, stdout, stderr){
            fakepid = stdout;
            console.log("PID = " + fakepid);
	     
	    var holder = fakepid.split("\n");
	    pid = holder[0];
	    console.log("New pid: "  + pid);
            if(err !== null){
                console.log("stderr: " + stderr);
                console.log("exec err: " + err);
            }
        });
    })
    socket.on('killProcess', function(msg){
	console.log(exec("ps -ef | grep '[B]'elle.py"));
        var child2 = exec("kill -2 " + pid, function(err, stdout, stderr){
            console.log("stdout: " + stdout);
            if(err !== null){
                console.log("stderr: " + stderr);
                console.log("exec err: " + err);
            }
        });
    })
})

http.listen(8080, function(){
    console.log("listening on 8080");
})

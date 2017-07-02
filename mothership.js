var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var exec = require('child_process').exec;

app.get('/mothership', function(req,res){
    res.sendFile(__dirname + ('/control.html'));
})

io.on('connection', function(socket){
    console.log("You have connected to the mothership");
    socket.on('testCommand', function(msg){
        var child = exec(msg, function(err, stdout, stderr){
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
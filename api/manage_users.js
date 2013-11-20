var port = 8005;
var express = require('express');
var app = express();

app.configure(function(){
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
});

app.get('/', function(req, res) {
  res.sendfile(__dirname + '/index.html');
});

app.post(/revoke-access/, function(req, res) {
  var uid = req.body.uid;
  var data = null;
  if (uid === "4") {
    res.send(200, 'Revoked access for ' + uid);
  }
  else {
    res.send(404, 'User not found');
  }
});

app.get('/tutorial-progress/:uid?', function(req, res) {
  var uid = req.params.uid;
  var data = null;

  if (uid === "4") {
    data = [{"num_lessons": 12, 
             "finished_time": "", 
             "title": "Developing Others", 
             "url": "/tutorials/developing-others", 
             "started_time": "2013-10-09", 
             "completed": false, 
             "num_completed_lessons": 2}];
  }
  else if (uid === "5") {
    data = [{"num_lessons": 16, 
             "finished_time": "", 
             "title": "Collaboration", 
             "url": "/tutorials/collaboration", 
             "started_time": "2013-10-07", 
             "completed": false,
             "num_completed_lessons": 0}, 
            {"num_lessons": 15, 
             "finished_time": "2013-10-16",
             "title": "Building Teams", 
             "url": "/tutorials/building-teams", 
             "started_time": "2013-10-02", 
             "completed": true, 
             "num_completed_lessons": 15}, 
            {"num_lessons": 12, 
             "finished_time": "", 
             "title": "Developing Others", 
             "url": "/tutorials/developing-others", 
             "started_time": "2013-10-07", 
             "completed": false, 
             "num_completed_lessons": 0}, 
            {"num_lessons": 23, 
             "finished_time": "",
             "title": "Change Management", 
             "url": "/tutorials/change-management",
             "started_time": "2013-10-02", 
             "completed": false, 
             "num_completed_lessons": 0}];
  }

  if (data) {
    res.json(data);
  }
  else {
    res.send(404, 'User not found');
  }
});


app.listen(port);

console.log('Server listening on port ' + port);

var port = 8005;
var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.sendfile(__dirname + '/index.html');
});

// url(r'^revoke-access/$', 'revoke_user_access', name='revoke_user_access'),
// url(r'^tutorial-progress/(?P<user_pk>\d+)/$', 'user_tutorial_progress', name='user_tutorial_progress'),
app.get('/tutorial-progress/:uid?', function(req, res) {
  var uid = req.params.uid;
  var data = [{"completed": true,
               "finished_time": "2013-10-09", 
               "num_completed_lessons": 12,
               "num_lessons": 12, 
               "started_time": "2013-10-09", 
               "title": "Developing Others", 
               "url": "/tutorials/developing-others"}];

  res.json(data);
});

app.configure(function(){
  app.use(express.logger('dev'));
});

app.listen(port);

console.log('Server listening on port ' + port);

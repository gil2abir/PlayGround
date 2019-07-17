var express = require('express');
var app = express();
var request = require('request');
const bodyParser = require('body-parser');
require('dotenv').config()
var localtunnel = require('localtunnel');

const accountSid = process.env.SID;
const authToken = process.env.KEY;
const client = require('twilio')(accountSid, authToken);
const MessagingResponse = require('twilio').twiml.MessagingResponse;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(__dirname + '/images'));

app.post('/incoming', (req, res) => {
  const twiml = new MessagingResponse();
  if (req.body.Body.toLowerCase().trim() != "hi" &&
    req.body.Body.toLowerCase().trim() != "hello" &&
    req.body.Body.toLowerCase().trim() != "test" &&
    req.body.Body.toLowerCase().trim() != "help") {
    request('https://api.duckduckgo.com/?skip_disambig=1&format=json&pretty=1&q=' + req.body.Body,
      function (error, response, body) {
        body = JSON.parse(body)
        console.log('body:', body["Abstract"]);
        console.log('raw: ', req);

        if (body["Abstract"] == "") {
          body["Abstract"] = body["RelatedTopics"][0]["Text"]
        }
        var msg = twiml.message(`*` + body["Heading"] + `*`+ body["Abstract"]);
        res.writeHead(200, { 'Content-Type': 'text/xml' });
        res.end(twiml.toString());
      });
  }
  else {
    var msg = twiml.message(`*Hey 👋*

I am a bot which summarizes WikiPedia pages to help you find quick information, right within WhatsApp.

Try it out - send me anything you want to know about`)
    res.writeHead(200, { 'Content-Type': 'text/xml' });
    res.end(twiml.toString());
  }

});

app.post('/check', function (req, res) {
  console.log(req.body.Body)
});
app.get('/', function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});

//var app = require('./app');
var serverless = require('serverless-http');
module.exports.handler = serverless(app);

//var listener = app.listen(Number(process.env.PORT), function() {
//  console.log('Your app is listening on port ' + listener.address().port);
//});

//var tunnel = localtunnel(parseInt(process.env.PORT, 10), {'subdomain' : process.env.SUBDOMAIN}, function(err, tunnel) {
//var tunnel = localtunnel(parseInt(process.env.PORT, 10), {'subdomain': process.env.SUBDOMAIN}, function(err, tunnel) {
//  if (err){
//      console.log('localtunnel didnt work')
//    }
//   
//  // the assigned public url for your tunnel
//  // i.e. https://abcdefgjhij.localtunnel.me
//  tunnel.url;
//  console.log('You can also use ' + tunnel.url);
//});
//   
//tunnel.on('close', function() {
//     // tunnels are closed
//});

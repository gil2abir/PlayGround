//This is shmul & gil's weather app

//Load some modules
const express = require('express')
const request = require('request')
const bodyParser = require('body-parser');
const APPKEY = "eeff7a051bda93c9ab1466473bffda33"
//config env'
const app = express()

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs')

app.get('/', function (req, res) {
    res.render('index', {weather: null, error: null});
})

app.post('/', function (req, res) {
    let city = req.body.city;
    let url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&units=imperial&appid=${APPKEY}`
  request(url, function (err, response, body) {
      if(err){
        res.render('index', {weather: null, error: 'Error, please try again'});
      } else {
        let weather = JSON.parse(body)
        if(weather.main == undefined){
          res.render('index', {weather: null, error: 'Error, please try again'});
        } else {
          let weatherText = `It's ${weather.main.temp} degrees in ${weather.name}! :D`;
          res.render('index', {weather: weatherText, error: null});
        }
      }
    });
  })

// 
app.listen(3333, function () {
  console.log('Example app listening on port 3333! http://localhost:3333')
})

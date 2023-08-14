#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const first = function () {
  request(url, function (error, response, body) {
    if (error) throw error;
    second(JSON.parse(body).characters, 0);
  });
};

const second = function (characters, i) {
  if (characters.length === i) {
    return;
  }
  request(characters[i], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    second(characters, ++i);
  });
};

first();

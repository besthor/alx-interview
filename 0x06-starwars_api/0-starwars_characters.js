#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes an API request to get film Information
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

// Parse the response body to get the list of character URLs
const charURLList = JSON.parse(body).characters;

// Iterate through the character URLs and fetc character information
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
       // Make a request to each character URl

      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parse the character information and print the character's name
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});

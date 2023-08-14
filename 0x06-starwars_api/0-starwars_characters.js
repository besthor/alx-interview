#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie
 * use star wars api
 */
const request = require('request');
const film_id = process.argv[2];
if (!film_id  || isNaN(film_id)) {
  process.exit(1);
}
const url = `https://swapi-api.hbtn.io/api/films/${film_id}`;

request(url, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characterList = [];

  const json = JSON.parse(body);
  const characters = json.characters;

  characters.forEach((character) => {
    const url = character;
    const promise = new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const json = JSON.parse(body);
        resolve(json.name);
      });
    });
    characterList.push(promise);
  });
  Promise.all(characterList).then((values) => {
    values.forEach((value) => {
      console.log(value);
    });
  }).catch((error) => {
    console.log(error);
  });
});

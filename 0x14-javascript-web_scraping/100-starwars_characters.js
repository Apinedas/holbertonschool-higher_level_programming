#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obtained = JSON.parse(body);
    for (const character of obtained.characters) {
      request(character, (charErr, charResponse, charBody) => {
        const obtainedChar = JSON.parse(charBody);
        console.log(obtainedChar.name);
      });
    }
  }
});

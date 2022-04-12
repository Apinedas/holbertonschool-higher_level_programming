#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const filmChars = [];

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obtained = JSON.parse(body);
    const totalCharacters = obtained.characters.length;
    for (const character of obtained.characters) {
      request(character, (charErr, charResponse, charBody) => {
        filmChars.push(JSON.parse(charBody));
        const actualLenght = filmChars.length;
        if (totalCharacters === actualLenght) {
          filmChars.sort((a, b) => {
            const aId = parseInt(a.url.split('/')[5]);
            const bId = parseInt(b.url.split('/')[5]);
            return aId - bId;
          });
          for (const actualChar of filmChars) {
            console.log(actualChar.name);
          }
        }
      });
    }
  }
});

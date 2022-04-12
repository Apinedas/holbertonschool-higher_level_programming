#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
let wedgeAntillesAppearances = 0;

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obtained = JSON.parse(body);
    for (const result of obtained.results) {
      for (const character of result.characters) {
        if (character.includes('/18/')) {
          wedgeAntillesAppearances += 1;
        }
      }
    }
    console.log(wedgeAntillesAppearances);
  }
});

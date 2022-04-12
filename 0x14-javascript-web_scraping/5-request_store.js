#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const fs = require('fs');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

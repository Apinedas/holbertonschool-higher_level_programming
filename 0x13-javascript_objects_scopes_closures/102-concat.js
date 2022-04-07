#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], (err, data) => {
  if (!err) {
    fs.writeFile(argv[4], data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

fs.readFile(argv[3], (err, data) => {
  if (!err) {
    fs.appendFile(argv[4], data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], 'utf-8', (err, data) => {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});

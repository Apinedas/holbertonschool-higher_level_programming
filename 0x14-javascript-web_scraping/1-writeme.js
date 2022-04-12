#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

#!/usr/bin/node
const { argv } = require('process');

const myNum = parseInt(argv[2]);

if (myNum) {
  console.log('My number: ' + myNum);
} else {
  console.log('Not a number');
}

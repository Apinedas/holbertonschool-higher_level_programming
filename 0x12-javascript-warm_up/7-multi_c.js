#!/usr/bin/node
const { argv } = require('process');
const printTimes = parseInt(argv[2]);
let i = 0;

if (printTimes) {
  while (i < printTimes) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

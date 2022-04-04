#!/usr/bin/node
const { argv } = require('process');
const squareSize = parseInt(argv[2]);
let i = 0;
let j = 0;
let line = '';

if (squareSize) {
  while (i < squareSize) {
    line += 'X';
    i++;
  }
  while (j < squareSize) {
    console.log(line);
    j++;
  }
} else {
  console.log('Missing size');
}

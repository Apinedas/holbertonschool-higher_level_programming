#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  const sum = a + b;
  return (sum);
}

const firstNum = parseInt(argv[2]);
const secondNum = parseInt(argv[3]);
const addition = add(firstNum, secondNum);

console.log(addition);

#!/usr/bin/node

const { argv } = require('process');

function factorial (a) {
  if (a) {
    return (a * factorial(a - 1));
  }
  return (1);
}

const num = parseInt(argv[2]);
const fact = factorial(num);

console.log(fact);

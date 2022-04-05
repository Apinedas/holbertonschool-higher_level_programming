#!/usr/bin/node

const { argv } = require('process');

function secondBiggestElement (a) {
  let biggest = 0;
  let secondBiggest = 0;
  let i = 0;
  let j = 0;

  while (a[i]) {
    if (biggest < a[i]) {
      biggest = a[i];
    }
    i++;
  }
  while (a[j]) {
    if (secondBiggest < a[j] && a[j] < biggest) {
      secondBiggest = a[j];
    }
    j++;
  }
  return (secondBiggest);
}

const nums = [];
let actualNum;
let k;

for (k = 0; argv[k]; k++) {
  actualNum = parseInt(argv[k]);
  if (actualNum) {
    nums.push(actualNum);
  }
}

console.log(secondBiggestElement(nums));

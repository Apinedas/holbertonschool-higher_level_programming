#!/usr/bin/node
const listFrom = require('./100-data').list;

const newList = listFrom.map((x, idx) => x * idx);
console.log(listFrom);
console.log(newList);

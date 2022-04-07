#!/usr/bin/node
const dictFrom = require('./101-data').dict;

const valuesList = Object.values(dictFrom);
const entriesList = Object.entries(dictFrom);
const dictTo = {};
valuesList.sort();
valuesList.forEach(element => {
    if (!(element in dictTo)){
        dictTo[element] = [];
    }
})
entriesList.forEach(entrie => {
    if (entrie[1] in dictTo) {
        dictTo[`${entrie[1]}`].push(entrie[0]);
    }
});
console.log(dictTo);

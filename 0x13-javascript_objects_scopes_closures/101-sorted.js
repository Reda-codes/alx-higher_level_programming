#!/usr/bin/node
const dict = require('./101-data').dict;

const newDct = {};
for (const key in dict) {
  if (newDct[dict[key]] === undefined) {
    newDct[dict[key]] = [];
  }
  newDct[dict[key]].push(key);
}
console.log(newDct);

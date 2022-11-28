#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

if ((process.argv.length - 2) < 2) {
  console.log('NaN');
} else {
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}

#!/usr/bin/node
function factorial (num) {
  let fct;
  if (num === 1) {
    return (num);
  } else {
    fct = num * factorial(num - 1);
    return fct;
  }
}

if (process.argv.length - 2 === 0) {
  console.log(1);
} else {
  console.log(factorial(process.argv[2]));
}

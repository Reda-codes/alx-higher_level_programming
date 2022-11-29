#!/usr/bin/node
const Base = require('./5-square');

class Square extends Base {
  charPrint (c) {
    if (c ===  undefined) {
      for (let i = 1; i <= this.height; i++) {
        let x = '';
        for (let j = 1; j <= this.width; j++) {
          x += 'X';
        }
        console.log(x);
      }
    } else {
      for (let i = 1; i <= this.height; i++) {
        let x = '';
        for (let j = 1; j <= this.width; j++) {
          x += 'c';
        }
        console.log(x);
      }
    }
  }
}

module.exports = Square;

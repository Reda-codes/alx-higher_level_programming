#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 1; i <= this.height; i++) {
        let x = '';
        for (let j = 1; j <= this.width; j++) {
          x += c;
        }
        console.log(x);
      }
    } else {
      for (let i = 1; i <= this.height; i++) {
        let x = '';
        for (let j = 1; j <= this.width; j++) {
          x += 'X';
        }
        console.log(x);
      }
    }
  }
}

module.exports = Square;

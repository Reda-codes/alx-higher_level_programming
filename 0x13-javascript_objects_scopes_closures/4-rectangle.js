#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      let x = '';
      for (let j = 1; j <= this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    const newH = this.width;
    const newW = this.height;
    this.width = newW;
    this.height = newH;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;

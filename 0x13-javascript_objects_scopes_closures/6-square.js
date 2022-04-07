#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i;
    let line = '';
    if (!c) {
      c = 'X';
    }
    for (i = 0; i < this.width; i++) {
      line += c;
    }
    for (i = 0; i < this.width; i++) {
      console.log(line);
    }
  }
};

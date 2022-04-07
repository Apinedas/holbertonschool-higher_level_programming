#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    let line = '';
    for (i = 0; i < this.width; i++) {
      line += 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(line);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
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
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

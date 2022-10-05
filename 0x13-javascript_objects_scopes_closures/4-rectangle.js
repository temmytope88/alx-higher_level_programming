#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
      for (let i = 1; i <= this.height; i++) {
        console.log('X'.repeat(this.width))
      }
    }

  rotate() {
    let height = this.height;
    let width = this.width
    this.height = width
    this.width = height
  }
  double() {
    let height = 2 * this.height;
    let width = 2 * this.width
    this.height = height
    this.width = width
  }
};

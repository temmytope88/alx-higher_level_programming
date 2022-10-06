#!/usr/bin/node
const square0 = require('./5-square');
module.exports = class Square extends square0 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 1; i <= this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};

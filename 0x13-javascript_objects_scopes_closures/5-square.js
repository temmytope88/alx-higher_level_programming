#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    const w = size;
    const h = size;
    super(w, h);
  }
};

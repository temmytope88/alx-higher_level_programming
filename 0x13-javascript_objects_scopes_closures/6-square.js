#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
	  constructor (size) {
		      const w = size;
		      const h = size;
		      super(w, h);
		    }

  charPrint (c) {
    if (c === 'undefined') {
      print();
    } else {
		 	for (let i = 1; i <= this.height; i++) {
				      console.log(c.repeat(this.width));
      }
    }
  }
};

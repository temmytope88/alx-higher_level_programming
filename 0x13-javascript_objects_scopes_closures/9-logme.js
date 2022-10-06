#!/usr/bin/node
let na = 0;
exports.logMe = function (item) {
	let value = na + ': ' + item;
	console.log(value);
	na++;
};


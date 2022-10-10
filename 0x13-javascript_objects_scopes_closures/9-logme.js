#!/usr/bin/node
let na = 0;
exports.logMe = function (item) {
  const value = na + ': ' + item;
  console.log(value);
  na++;
};

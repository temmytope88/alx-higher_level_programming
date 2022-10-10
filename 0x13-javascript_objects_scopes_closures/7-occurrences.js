#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let value = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      value = value + 1;
    }
  }
  return value;
};

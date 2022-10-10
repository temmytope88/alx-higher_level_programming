#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  const n = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    const j = n - i;
    arr[j] = list[i];
  }
  return arr;
};

#!/usr/bin/node
const a = process.argv;

if (a.length <= 3) {
  console.log(0);
} else {
  const b = a.slice(2);
  const d = b.sort(function (a, b) { return b - a; });
  console.log(d[1]);
}

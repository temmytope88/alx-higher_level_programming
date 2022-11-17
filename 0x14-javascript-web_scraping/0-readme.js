#!/usr/bin/node

const fs = require('fs');
// Asynchronous read
const file = process.argv[2];

fs.readFile(file, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});

#!/usr/bin/node

var fs = require("fs");
// Asynchronous read
var file = process.argv[2];

fs.readFile(file, function (err, data) {

   if (err) {
      return console.error(err);
   }
   console.log(data.toString());
});
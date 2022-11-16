#!/usr/bin/node
const fs = require("fs")
var file = process.argv[2]
var data = process.argv[3]
fs.writeFile(file, data, function(err){
  if(err) throw err
})
#!/usr/bin/node
const request = require("requests")
let url = process.argv[2]
request.get(url, (error, res) => {
  if(error){
    console.log(error)
  }
  else{
    console.log(res.statusCode)
  }
})
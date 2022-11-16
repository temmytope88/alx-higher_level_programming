#!/usr/bin/node
const request = require("request")
// Request URL
let url = process.argv[2]

request(url, (error, response, body)=>{

    // Printing the error if occurred
    if(error){
      console.log(error)
    }
    // Printing status code
    else{
      console.log('code: ' + response.statusCode);
    }
});
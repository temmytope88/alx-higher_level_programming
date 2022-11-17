#!/usr/bin/node
const request = require('request');
// Request URL
const url = process.argv[2];

request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

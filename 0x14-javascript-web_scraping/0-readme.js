#!/usr/bin/node
// Scripts to reads and print files contents

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

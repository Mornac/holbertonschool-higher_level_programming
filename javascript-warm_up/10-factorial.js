#!/usr/bin/node
const { argv } = require('node:process');

function fact (n) {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}
console.log(fact(argv[2]));

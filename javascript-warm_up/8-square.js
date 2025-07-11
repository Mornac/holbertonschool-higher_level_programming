#!/usr/bin/node
const size = parseInt(process.argv[2]);
let line = '';
let i;
let j;

if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (i = 0; i < size; i++) {
    line += 'X';
  }
  for (j = 0; j < size; j++) {
    console.log(line);
  }
}

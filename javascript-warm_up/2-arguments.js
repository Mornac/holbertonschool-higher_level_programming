#!/usr/bin/node
const string = process.argv.length;
if (string === 2) {
    console.log('No argument');
}
else if (string === 3) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}

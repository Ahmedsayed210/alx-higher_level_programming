#!/usr/bin/node
const numArg = process.argv.lenght;
if (numArg === 2) {
  console.log('No argument');
} else if (numArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

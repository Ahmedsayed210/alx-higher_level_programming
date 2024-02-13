#!/usr/bin/node
const [, , numArg] = process.argv;
parseInt(numArg);
if (!isNaN(numArg)) {
  console.log(`My number: ${numArg}`);
} else {
  console.log('Not a number');
}

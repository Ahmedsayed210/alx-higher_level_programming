#!/usr/bin/node
const [, , numArg] = process.argv;
parseInt(numArg);
const C = 'C is fun';
if (!isNaN(numArg)) {
  for (let i = 0; i < numArg; i++) {
    console.log(C);
  }
} else {
  console.log('Missing number of occurrences');
}

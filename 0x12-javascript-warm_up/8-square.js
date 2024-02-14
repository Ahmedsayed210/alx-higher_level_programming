#!/usr/bin/node
const [, , sizeSquare] = process.argv;
parseInt(sizeSquare);
if (!isNaN(sizeSquare)) {
  for (let i = 0; i < sizeSquare; i++) {
    console.log('X'.repeat(sizeSquare));
  }
} else {
  console.log('Missing size');
}

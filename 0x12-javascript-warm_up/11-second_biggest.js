#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const integers = args.map(Number);
  let firstMax = integers[0];
  let secondMax = Number.MIN_SAFE_INTEGER;

  for (let i = 1; i < integers.length; i++) {
    if (integers[i] > firstMax) {
      secondMax = firstMax;
      firstMax = integers[i];
    } else if (integers[i] > secondMax && integers[i] !== firstMax) {
      secondMax = integers[i];
    }
  }

  console.log(secondMax);
}

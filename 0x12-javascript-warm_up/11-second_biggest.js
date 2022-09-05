#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
if (Number.isNaN(arg1)) {
  console.log(0);
} else {
  console.log(`My number: ${arg1}`);
}

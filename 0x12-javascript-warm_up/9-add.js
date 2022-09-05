#!/usr/bin/node
const args = process.argv;
function add (x, y) {
  console.log(parseInt(x) + parseInt(y));
}
add(args[2], args[3]);

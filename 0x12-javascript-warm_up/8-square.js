#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let str;
    str = '';
    for (let j = 0; j < x; j++) {
      str += 'X';
    }
    console.log(str);
  }
}

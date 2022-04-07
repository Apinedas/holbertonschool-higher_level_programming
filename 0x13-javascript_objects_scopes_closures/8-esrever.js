#!/usr/bin/node
exports.esrever = function (list) {
  let len;
  const copy = [];
  let aux = 0;
  for (len = 0; list[len]; len++) {
    continue;
  }
  for (len -= 1; len >= 0; len--, aux++) {
    copy[aux] = list[len];
  }
  return (copy);
};

#!/usr/bin/node
exports.esrever = function (list) {
  let len;
  let copy;
  let aux;
  for (len = 0; list[len]; len++) {
    continue;
  }
  if (len <= 1) {
    return (list);
  }
  for (copy = 0; copy < len; copy++, len--) {
    aux = list[copy];
    list[copy] = list[len - 1];
    list[len] = aux;
  }
  return (list);
};

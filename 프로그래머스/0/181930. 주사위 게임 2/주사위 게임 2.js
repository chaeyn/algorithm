function solution(a, b, c) {
  let res = 0;
  if (a === b && b === c) {
    res = (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c);
  } else if (a !== b && a !== c && b !== c) {
    res = a + b + c;
  } else {
    res = (a + b + c) * (a * a + b * b + c * c);
  }
  return res;
}

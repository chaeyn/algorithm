function solution(n) {
  let ans = 0;
  if (n % 2 !== 0) {
    for (let i = 1; i <= n; i += 2) {
      ans += i;
    }
  } else {
    for (let i = 2; i <= n; i += 2) {
      ans += i * i;
    }
  }
  return ans;
}

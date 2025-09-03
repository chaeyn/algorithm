function solution(ineq, eq, n, m) {
  switch (true) {
    case ineq === ">" && eq === "=":
      if (n >= m) return 1;
      else return 0;
    case ineq === "<" && eq === "=":
      if (n <= m) return 1;
      else return 0;
    case ineq === "<" && eq === "!":
      if (n < m) return 1;
      else return 0;
    case ineq === ">" && eq === "!":
      if (n > m) return 1;
      else return 0;
  }
}

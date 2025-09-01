function solution(a, b) {
    let sum1 = Number(String(a)+String(b));
    let sum2 = Number(String(b)+String(a));
    if (sum1 >= sum2) {
        return sum1
    } else return sum2
}
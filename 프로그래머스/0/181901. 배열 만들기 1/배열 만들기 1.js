function solution(n, k) {
    let arr = [];
    for (let i = k; i <= n; i+=k) {
        arr.push(i);
    }
    return arr
}
function solution(num_list) {
    let mul = num_list.reduce((a, b) => (a * b));
    let sum = num_list.reduce((a, b) => (a + b));
    // 배열 안 원소를 다루는 것은 reduce 메서드 사용
    if (mul < sum*sum) {
        return 1
    } else return 0
}
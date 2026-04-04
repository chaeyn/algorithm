function solution(my_string, is_prefix) {
    return +my_string.startsWith(is_prefix)
    // startsWith -> 문자열이 접두사로 시작하는지 확인
    // boolean 반환값에 + 추가하면 true = 1, false = 0으로 반환
}
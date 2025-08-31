const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', function (line) {
    let str = [line][0];
    [...str].forEach((c) => console.log(c));
    // ... str을 모두 포함 a b c d e, [...str] -> ["a", "b", "c", "d", "e"]
    // forEach 메서드는 ((c) => console.log(c)) 각 배열 요소에 대해 함수를 한 번씩 실행


})
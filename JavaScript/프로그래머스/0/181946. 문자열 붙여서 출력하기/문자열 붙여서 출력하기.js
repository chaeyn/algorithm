const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', function (line) {
    console.log(line.split(' ').join(""));
    // spilt -> 공백으로 배열 분리
    // join -> 배열을 빈 문자열로 합치기
})
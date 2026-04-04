const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', function (line) {
    let [a, b] = line.split(' ');
    console.log(`${a} + ${b} = ${Number(a)+Number(b)}`)
})
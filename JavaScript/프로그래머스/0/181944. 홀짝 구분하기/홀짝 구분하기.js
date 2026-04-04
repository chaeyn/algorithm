const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', function (line) {
    n = +(line);
    const res = n % 2 === 0 ? "even" : "odd";
    console.log(`${n} is ${res}`);
})
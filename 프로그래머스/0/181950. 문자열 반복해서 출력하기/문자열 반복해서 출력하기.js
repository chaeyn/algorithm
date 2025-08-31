const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', function (line) {
    const [str, n] = line.split(' ');
    console.log(str.repeat(n))
})
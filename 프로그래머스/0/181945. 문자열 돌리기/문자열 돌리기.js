const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}).on('line', function (line) {
    let str = [line][0];
    for (let i = 0; i < str.length; i++) {
        console.log(str[i]);
    }
})
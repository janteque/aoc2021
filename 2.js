const readline = require('readline');
const fs = require('fs');

var file = './input_2.txt';

var countA = 0;
var countB = 0;
var line_number = 0;

const U = "up";
const D = "down";
const F = "forward";

var depth = 0;
var aim = 0;
var x = 0;

async function processLineByLine() {

    var rl = readline.createInterface({
        input : fs.createReadStream(file),
        output : process.stdout,
        terminal: false
    });

    var last = 0;
    var lastAgg = 0;
    
    rl.on('line', function (line) {
        line_number++
        const lineArray = line.split(" ");
        var instruction = lineArray[0]
        var metric = parseInt(lineArray[1])
        var n = parseInt(line)

        switch (instruction) {
            case U:
                aim = aim - metric;
                break;
            case D:
                aim = aim + metric;
                break;
            case F:
                x = x + metric;
                depth = depth + aim*metric;
                break;
        }

        
    });

    rl.on('close', function () {
        console.log(`A: ${depth*x}`)
    });
}

 processLineByLine();


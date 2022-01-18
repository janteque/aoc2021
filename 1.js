const readline = require('readline');
const fs = require('fs');



var file = './input_1.txt';

var countA = 0;
var countB = 0;
var line_number = 0;

const slideSize = 3;

var slideAggs = []

var slides = []

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
        var n = parseInt(line)

        slides.push([n]);

        if (slides.length > 1){
            slides[slides.length-2].push(n)
        }
        if (slides.length > 2){
            slides[slides.length-3].push(n)
            var lastSum = slides[slides.length-3].reduce((a, b) => a + b, 0)
           // console.log(`sum ${lastSum}`)
        }

        if(last != 0 && n>last){
            countA++
        }
        if(lastAgg != 0 && lastSum>lastAgg){
            countB++
        }        
        last = n;
        lastAgg = lastSum;
        
    });

    rl.on('close', function () {
        console.log(`A: ${countA}`)
        console.log(`B: ${countB}`)
    });
}

 processLineByLine();


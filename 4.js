const readline = require('readline');
const fs = require('fs');

var file = './input_4.txt';

var bingonumbers = [];

var cartones = [];

function calculateGamma(dataArray, binarysize)
{
    var gamma = 0;
    var epsilon = 0;
    var ocurrences1 = [];
    var ocurrences0 = [];
    var masksarray = [];


    for (let index = binarysize; index > 0; index--) {
        masksarray.push(1<<(index-1))
        ocurrences1.push(0)
        ocurrences0.push(0)
    }
    //masksarray= [10000, 01000, 00100, 00010, 00001]

    dataArray.forEach(element => {
        var pos = 0;
        masksarray.forEach(mask => {
            if(element & mask){
                ocurrences1[pos]++;
            }else{
                ocurrences0[pos]++;
            }
            pos++
        });
    });

    var pos = 0;
    ocurrences1.forEach(occ1 => {
        if (occ1 >= ocurrences0[pos]) { //set gamma at 1
           gamma = gamma | (1 << (binarysize-pos-1));
        }
        else {
           epsilon = epsilon | (1 << (binarysize-pos-1));
        }
        pos++;
    });

    return {gamma:gamma, epsilon:epsilon};
}

async function processLineByLine() {

    var rl = readline.createInterface({
        input: fs.createReadStream(file),
        output: process.stdout,
        terminal: false
    });


    rl.on('line', function (line) {
        //console.log(`line ${line}: ${parseInt(line,2)}`)
        data.push(parseInt(line,2))
        const lineArray = line.split("");
        var pos = 0;
        lineArray.forEach(element => {
            if (element === '0')
                ocurrences0[pos]++
            else
                ocurrences1[pos]++
            pos++
        });


    });

    rl.on('close', function () {
        var pos = 0;
        ocurrences1.forEach(occ1 => {
            if (ocurrences0[pos] > occ1) {
                gammaArray[pos] = 0;
                epsilomArray[pos] = 1;
            }
            else {
                gammaArray[pos] = 1;
                epsilomArray[pos] = 0;
            }
            pos++;
        });

        console.log(`gammabinary: ${gammaArray.join("")}`)
        console.log(`epsilombinary: ${epsilomArray.join("")}`)

        var gamma = parseInt(gammaArray.join(""), 2);
        var epsilom = parseInt(epsilomArray.join(""), 2);

        console.log(`(A) gamma: ${gamma} epsilom: ${epsilom}`)
        
        console.log(`(A) ${gamma*epsilom}`)

        let result = calculateGamma(data, inputbinarySize);
        console.log(`(A BIS) gamma: ${result.gamma} epsilom: ${result.epsilon}`)
        console.log(`(A BIS) gamma: ${result.gamma.toString(2)} epsilom: ${result.epsilon.toString(2)}`)


        var filteredO2 = [...data];
        var filteredCO2 = [...data];

        var ox_gen_rat;
        var co2_scu_rat;

        masksarray.forEach(mask => {
            var gammaO2 = calculateGamma(filteredO2, inputbinarySize).gamma;
            var gammaCO2 = calculateGamma(filteredCO2, inputbinarySize).gamma;

            if(gammaO2 & mask){
                filteredO2 = filteredO2.filter(element => (element & mask));
            }else{
                filteredO2 = filteredO2.filter(element => !(element & mask));
            }

            if((gammaCO2 & mask)){ //position is not a 0
                filteredCO2 = filteredCO2.filter(element => !(element & mask)); //filter elements with 1
            }else{
                filteredCO2 = filteredCO2.filter(element => (element & mask)); //filter elements with not 1
            }


            if(filteredO2.length == 1){
                console.log(`(B filteredO2) ${filteredO2}`)
                ox_gen_rat = filteredO2[0]
            }

            if(filteredCO2.length == 1){
                console.log(`(B filteredCO2) ${filteredCO2}`)
                co2_scu_rat = filteredCO2[0]
            }
        });

        console.log(`(B result: ) ${ox_gen_rat*co2_scu_rat}`)
        

    });
}

processLineByLine();


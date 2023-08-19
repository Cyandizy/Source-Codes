const input = document.getElementById("input");
let operator;
let inputString = "";
let result;
let operatorInput = false;
let operatorInputStartedWithMinus = false;
let splittedNumber;
let infoText = false;

function inputNumber(x) {
    input.style.fontSize = "250%";
    if (infoText == true) {
        input.innerHTML = "";
        infoText = false;
    }
    inputString += x;
    input.innerHTML += x;
    console.log(inputString);
}

function inputOperator(x) {
    input.style.fontSize = "250%";
    if (infoText == true) {
        input.innerHTML = "";
        infoText = false;
    }   
    if (inputString == "" && x == "\u221A") {
        console.log("\u221A");
        operator = "sqrt";
        inputString += "sqrt";
        input.innerHTML += x;
        operatorInput = true;
    }
    else {

        if (inputString.startsWith('-')) {

            if (operatorInputStartedWithMinus == false) {

                input.innerHTML += x;

                if (x == '\u00D7') {
                    console.log("&times;")
                    inputString += '*';
                    operator = '*';
                }
                else if (x == '\u00F7') {
                    console.log("&divide;")
                    inputString += '/';
                    operator = '/';
                }
                else {
                    inputString += x;
                    operator = x;
                }
                operatorInput = true;
                operatorInputStartedWithMinus = true;

                if (operatorInputStartedWithMinus == true) {
                    console.log("startedWithMinus == true")
                }
            }
        }
        else if (operatorInput == false) {
            input.innerHTML += x;
            if (x == '\u00D7') {
                console.log("&times;")
                inputString += '*';
                operator = '*';
            }
            else if (x == '\u00F7') {
                console.log("&divide;")
                inputString += '/';
                operator = '/';
            }
            else {
                inputString += x;
                operator = x;
            }
            operatorInput = true;
            console.log(inputString);
            console.log("if")
        }
    }
}

function process() {
    splittedNumber = inputString.split(/[\+\-\*\/\"sqrt"]/);
    splittedNumber = splittedNumber.filter(Boolean);
    console.log(splittedNumber);

    if (operatorInputStartedWithMinus == true) {
        splittedNumber[0] = "-" + splittedNumber[0];
        console.log(splittedNumber);
    }

    if (operator == '+') {
        result = Number(splittedNumber[0]) + Number(splittedNumber[1]);
        console.log(result);
        inputString = result.toString();
        input.innerHTML = inputString;
    }
    else if (operator == '-') {
        result = Number(splittedNumber[0]) - Number(splittedNumber[1]);
        console.log(result);
        inputString = result.toString();
        input.innerHTML = inputString;
    }
    else if (operator == '*') {
        result = Number(splittedNumber[0]) * Number(splittedNumber[1]);
        console.log(result);
        inputString = result.toString();
        input.innerHTML = inputString;
    }
    else if (operator == '/') {
        result = Number(splittedNumber[0]) / Number(splittedNumber[1]);
        console.log(result);
        inputString = result.toString();
        input.innerHTML = inputString;
    }
    else if (operator == 'sqrt'){
        result = Math.sqrt(Number(splittedNumber[0]));
        console.log(result);
        inputString = result.toString();
        input.innerHTML = inputString;
    }
    else if (operator == ''){
        //pass
    }
    operator = '';
    operatorInput = false;
    operatorInputStartedWithMinus = false;
}

function inputClear() {
    inputString = "";
    input.innerHTML = inputString;
    operatorInput = false;
    operatorInputStartedWithMinus = false;
}

function inputPop() {
    inputString = inputString.slice(0, -1);
    input.innerHTML = inputString;
    if (inputString.includes('+') == false || inputString.includes('-') == false || 
        inputString.includes('*') == false || inputString.includes('/') == false) {
            operatorInput = false;
            operatorInputStartedWithMinus = false;
    }
}

function openPopUp() {
    input.style.fontSize = "90%";
    input.innerHTML = "//Use '\u221A' before numbers <br><br> made by Komes Pispol";
    infoText = true;
    inputString = "";
    operator = '';
    operatorInput = false;
    operatorInputStartedWithMinus = false;
}
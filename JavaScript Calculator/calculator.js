let input = document.getElementById("input");
let operator;
let input_string = "";
let result;
let operator_input = false;
let operator_input_started_with_minus = false;
let splitted_number;
let info_text = false;

function input_number(x) {
    input.style.fontSize = "250%";
    if (info_text == true) {
        input.innerHTML = "";
        info_text = false;
        console.log("info_text = false")
    }
    input_string += x;
    input.innerHTML += x;
    console.log(input_string);
}

function input_operator(x) {
    input.style.fontSize = "250%";
    if (info_text == true) {
        input.innerHTML = "";
        info_text = false;
    }   
    if (input_string == "" && x == "\u221A") {
        console.log("\u221A");
        operator = "sqrt";
        input_string += "sqrt";
        input.innerHTML += x;
        operator_input = true;
    }
    else {

        if (input_string.startsWith('-')) {

            if (operator_input_started_with_minus == false) {

                input.innerHTML += x;

                if (x == '\u00D7') {
                    console.log("&times;")
                    input_string += '*';
                    operator = '*';
                }
                else if (x == '\u00F7') {
                    console.log("&divide;")
                    input_string += '/';
                    operator = '/';
                }
                else {
                    input_string += x;
                    operator = x;
                }
                operator_input = true;
                operator_input_started_with_minus = true;

                if (operator_input_started_with_minus == true) {
                    console.log("started_with_minus == true")
                }
            }
        }
        else if (operator_input == false) {
            input.innerHTML += x;
            if (x == '\u00D7') {
                console.log("&times;")
                input_string += '*';
                operator = '*';
            }
            else if (x == '\u00F7') {
                console.log("&divide;")
                input_string += '/';
                operator = '/';
            }
            else {
                input_string += x;
                operator = x;
            }
            operator_input = true;
            console.log(input_string);
            console.log("if")
        }
    }
}

function process() {
    splitted_number = input_string.split(/[\+\-\*\/\"sqrt"]/);
    splitted_number = splitted_number.filter(Boolean);
    console.log(splitted_number);

    if (operator_input_started_with_minus == true) {
        splitted_number[0] = "-" + splitted_number[0];
        console.log(splitted_number);
    }

    if (operator == '+') {
        result = Number(splitted_number[0]) + Number(splitted_number[1]);
        console.log(result);
        input_string = result.toString();
        input.innerHTML = input_string;
    }
    else if (operator == '-') {
        result = Number(splitted_number[0]) - Number(splitted_number[1]);
        console.log(result);
        input_string = result.toString();
        input.innerHTML = input_string;
    }
    else if (operator == '*') {
        result = Number(splitted_number[0]) * Number(splitted_number[1]);
        console.log(result);
        input_string = result.toString();
        input.innerHTML = input_string;
    }
    else if (operator == '/') {
        result = Number(splitted_number[0]) / Number(splitted_number[1]);
        console.log(result);
        input_string = result.toString();
        input.innerHTML = input_string;
    }
    else if (operator == 'sqrt'){
        result = Math.sqrt(Number(splitted_number[0]));
        console.log(result);
        input_string = result.toString();
        input.innerHTML = input_string;
    }
    else if (operator == ''){
        //pass
    }
    operator = '';
    operator_input = false;
    operator_input_started_with_minus = false;
}

function input_clear() {
    input_string = "";
    input.innerHTML = input_string;
    operator_input = false;
    operator_input_started_with_minus = false;
}

function input_pop() {
    input_string = input_string.slice(0, -1);
    input.innerHTML = input_string;
    if (input_string.includes('+') == false || input_string.includes('-') == false || 
        input_string.includes('*') == false || input_string.includes('/') == false) {
            operator_input = false;
            operator_input_started_with_minus = false;
    }
}

function open_popup() {
    input.style.fontSize = "90%";
    input.innerHTML = "//Use '\u221A' before numbers <br><br> made by Komes Pispol";
    info_text = true;
    input_string = "";
    operator = '';
    operator_input = false;
    operator_input_started_with_minus = false;
}
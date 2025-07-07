const myText = document.getElementById("myText");
const mySubmit = document.getElementById("mySubmit");
const resultElement = document.getElementById("resultElement");

let age = 0;

mySubmit.onclick = function () {

    age = myText.value /* input box is ALWAYS a STRING--> convert to int*/
    age = Number(age);

    if (age >= 100) {
        resultElement.textContent = `You are too old for this`
    }
    else if (age == 0) {
        resultElement.textContent = `You cant be a baby for this`
    }
    else if (age >= 18) {
        resultElement.textContent = `You a are fit for this`;
    }
    else if (age < 0) {
        resultElement.textContent = `You have not been born yet`;

    } else {
        resultElement.textContent = ` You are too young for this`
    }
}
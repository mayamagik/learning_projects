// DICE ROLLER

function rollDice() {

    const numOfDice = document.getElementById("numOfDice").value;
    const diceResult = document.getElementById("diceResult");
    const dicePics = document.getElementById("dicePics");
    const values = [];
    const pics = [];

    for (let i = 0; i < numOfDice; i++) {
        const value = Math.floor(Math.random() * 6) + 1;
        values.push(value);
        pics.push(`<img src="dicePics/${value}.png">`); //alt="Dice ${value} --> add this inside tag for alternative display in case pics don't work

    }

    diceResult.textContent = `dice: ${values.join(', ')}`;
    dicePics.innerHTML = pics.join('')


}
// PASSWORD GENERATOR

// CREATE FUNCTION WITH PARAMETERS FOR CONTENT OF PASSWORD
function generatePassword(length, includeLowerCase, includeUpperCase, includeNumbers, includeSymbols) {

    const lowerCaseChars = "abcdefghijklmnopqrstuvwxyz";
    const upperCaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numberChars = "0123456789";
    const symbolChars = ".,;:_+=?%$&/*^#"

    // CREATE EMPTY POOL OF ALLOWED CHARS & EMPTY PASSWORD

    let allowedChars = "";
    let password = "";

    // CONCATENATE CHARS & ADD THEM TO THE POOL IN CASE OPTIONS ARE SET TO TRUE; IF NOT LEAVE EMPTY

    allowedChars += includeLowerCase ? lowerCaseChars : "";
    allowedChars += includeUpperCase ? upperCaseChars : "";
    allowedChars += includeNumbers ? numberChars : "";
    allowedChars += includeSymbols ? symbolChars : "";

    // FORMULATE EXCEPTIONS REGARDING ALLOWED LENGTH
    if (length <= 0) {
        return `(password length must be at least 1 character)`;

    }
    if (allowedChars.length === 0) {
        return `(At least 1 set of characters needs to be selected)`;
    }
    // LOOP 12 TIMES AND ADD EACH RANDOM CHAR TO THE PASSWORD
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * allowedChars.length);
        password += allowedChars[randomIndex];
    }

    return password;
}

// LEAVE CONFIGURATION VARIABLES TO THE END FOR READABILITY
const passwordLength = 12;
const includeLowerCase = true;
const includeUpperCase = true;
const includeNumbers = true;
const includeSymbols = true;

// CALL FUNCTION AND STORE IT IN THE PASSWORD
const password = generatePassword(passwordLength, includeLowerCase, includeUpperCase, includeNumbers, includeSymbols);

console.log(`Generated password: ${password}`);

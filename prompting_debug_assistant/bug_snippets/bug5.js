function doubleInput(inputString) {
    // Bug: Concatenates string instead of adding numbers
    let value = inputString;
    return value + value;
}

console.log(doubleInput("10")); // Intended: 20, Actual: "1010"

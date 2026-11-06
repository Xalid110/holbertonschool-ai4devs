// Fixed version of bug5.js

function processTransactionAmount(rawAmountString) {
    // Fixed: Converted input string to a number to avoid concatenation
    let processedValue = Number(rawAmountString);
    let doubledValue = processedValue + processedValue;
    
    return doubledValue;
}

// Running verification test
let userEntry = "50";
let result = processTransactionAmount(userEntry);

console.log("Expected result: 100");
console.log("Actual result: " + result);

console.assert(result === 100, "Validation failed: Expected 100");

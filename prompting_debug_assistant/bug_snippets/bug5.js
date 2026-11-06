// Function to double a numeric value provided as a string from an input
function processTransactionAmount(rawAmountString) {
    console.log("Processing input value: " + rawAmountString);
    
    // Bug: Type confusion - string concatenation instead of numeric addition
    let processedValue = rawAmountString;
    let doubledValue = processedValue + processedValue;
    
    return doubledValue;
}

// Running verification test
let userEntry = "50";
let result = processTransactionAmount(userEntry);

console.log("Expected result: 100");
console.log("Actual result: " + result);

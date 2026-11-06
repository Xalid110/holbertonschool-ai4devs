// Function to generate a sequence of numbers up to limit n
// Intended behavior: Print all numbers from 1 up to and including n

function printSequence(limit) {
    console.log("Starting sequence printing up to " + limit);
    
    // Bug: Off-by-one error (condition i < limit excludes the number limit itself)
    for (let i = 1; i < limit; i++) {
        console.log("Current item: " + i);
    }
    
    console.log("Sequence printing complete.");
}

// Executing test cases
const targetLimit = 5;
printSequence(targetLimit);
// Expected output: 1, 2, 3, 4, 5

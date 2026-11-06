// Fixed version of bug2.js

function printSequence(limit) {
    console.log("Starting sequence printing up to " + limit);
    
    // Fixed: Loop condition changed from i < limit to i <= limit
    for (let i = 1; i <= limit; i++) {
        console.log("Current item: " + i);
    }
    
    console.log("Sequence printing complete.");
}

// Executing test case
const targetLimit = 5;
printSequence(targetLimit);

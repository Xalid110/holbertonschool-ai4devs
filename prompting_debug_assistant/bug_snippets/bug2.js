function printNumbersUpTo(n) {
    // Bug: Off-by-one error (< instead of <=)
    for (let i = 1; i < n; i++) {
        console.log(i);
    }
}

printNumbersUpTo(5); // Intended output: 1, 2, 3, 4, 5

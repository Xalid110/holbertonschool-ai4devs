#include <iostream>
#include <vector>

// Function to sum all elements inside a std::vector
int calculate_sum(const std::vector<int>& numbers) {
    int total = 0;
    
    // Bug: Missing namespace prefix for vector iterator and broken increment syntax
    for (vector<int>::const_iterator it = numbers.begin(); it != numbers.end(); it+) {
        total += *it;
    }
    
    return total;
}

int main() {
    std::vector<int> data = {10, 20, 30, 40, 50};
    int result = calculate_sum(data);
    
    std::cout << "Total Sum: " << result << std::endl;
    return 0;
}

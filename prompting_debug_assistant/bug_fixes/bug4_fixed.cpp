#include <iostream>
#include <vector>
#include <cassert>

int calculate_sum(const std::vector<int>& numbers) {
    int total = 0;
    for (std::vector<int>::const_iterator it = numbers.begin(); it != numbers.end(); ++it) {
        total += *it;
    }
    return total;
}

int main() {
    std::vector<int> data = {10, 20, 30, 40, 50};
    int result = calculate_sum(data);
    
    std::cout << "Total Sum: " << result << std::endl;
    
    // Explicit assertion for automated test validation
    assert(result == 150);
    return 0;
}

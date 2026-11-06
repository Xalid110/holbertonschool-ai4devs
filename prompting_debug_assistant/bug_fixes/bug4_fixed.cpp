#include <iostream>
#include <vector>

// Fixed version of bug4.cpp
int calculate_sum(const std::vector<int>& numbers) {
    int total = 0;
    
    // Fixed: Added std:: namespace prefix and fixed increment syntax (++it)
    for (std::vector<int>::const_iterator it = numbers.begin(); it != numbers.end(); ++it) {
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

#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    int total = 0;

    // Bug: Missing std:: prefix and broken loop syntax
    for (vector<int>::iterator it = numbers.begin(); it != numbers.end(); it+) {
        total += *it;
    }

    std::cout << "Sum: " << total << std::endl;
    return 0;
}

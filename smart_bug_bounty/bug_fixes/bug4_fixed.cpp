
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

int findMaximum(const vector<int>& numbers) {
    if (numbers.empty()) {
        throw invalid_argument("Vector cannot be empty");
    }

    int maximum = numbers[0];

    for (size_t i = 1; i < numbers.size(); i++) {
        if (numbers[i] > maximum) {
            maximum = numbers[i];
        }
    }

    return maximum;
}

int main() {
    assert(findMaximum({12, 45, 23, 67, 34}) == 67);
    assert(findMaximum({5}) == 5);
    assert(findMaximum({-10, -2, -30}) == -2);
    assert(findMaximum({1, 1, 1}) == 1);

    cout << "All bug4 tests passed!" << endl;
    return 0;
}

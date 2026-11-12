
#include <iostream>
#include <vector>
using namespace std;

int findMaximum(const vector<int>& numbers) {
    int maximum = numbers[0];

    for (int i = 1; i <= numbers.size(); i++) {
        if (numbers[i] > maximum) {
            maximum = numbers[i];
        }
    }

    return maximum;
}

int main() {
    vector<int> values = {12, 45, 23, 67, 34};

    cout << "Maximum: " << findMaximum(values) << endl;

    return 0;
}

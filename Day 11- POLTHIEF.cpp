#include <iostream>
#include <vector>
#include <cmath> // for abs function

using namespace std;

int main() {
    int T;
    cin >> T; // Read the number of test cases
    vector<int> results(T);

    for (int i = 0; i < T; ++i) {
        int X, Y;
        cin >> X >> Y; // Read the positions of policeman and thief
        // Calculate the time to catch the thief
        results[i] = abs(Y - X) / 1; // Relative speed difference is 1 unit per second
    }

    for (int result : results) {
        cout << result << endl; // Output results for each test case
    }

    return 0;
}

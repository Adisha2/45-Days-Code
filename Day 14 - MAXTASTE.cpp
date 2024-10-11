#include <iostream>
#include <algorithm> // for std::max
using namespace std;

int main() {
    int T; // Number of test cases
    cin >> T;

    while (T--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        // Calculate all possible combinations
        int tastiness1 = a + c;
        int tastiness2 = a + d;
        int tastiness3 = b + c;
        int tastiness4 = b + d;

        // Find the maximum tastiness
        int max_tastiness = max({tastiness1, tastiness2, tastiness3, tastiness4});

        // Print the result for this test case
        cout << max_tastiness << endl;
    }

    return 0;
}

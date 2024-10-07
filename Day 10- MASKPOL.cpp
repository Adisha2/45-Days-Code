#include <iostream>
#include <algorithm> // for std::min

using namespace std;

int main() {
    int T;
    cin >> T; // Number of test cases
    while (T--) {
        int N, A;
        cin >> N >> A; // Read total people and infected people
        int U = N - A; // Calculate uninfected people
        cout << min(A, U) << endl; // Output the minimum number of masks needed
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;  // Read the number of test cases

    while (T--) {
        int N;
        cin >> N;  // Read the length of the string
        string S;
        cin >> S;  // Read the string

        // Step 1: Swap characters in pairs
        for (int i = 0; i < N - 1; i += 2) {
            swap(S[i], S[i + 1]);
        }

        // Step 2: Replace each character
        for (char &c : S) {
            c = char(219 - int(c));  // Using the formula to replace characters
        }

        // Output the encoded message
        cout << S << endl;
    }

    return 0;
}

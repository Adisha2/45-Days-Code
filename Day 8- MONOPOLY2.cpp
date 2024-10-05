#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T; // Read the number of test cases
    vector<string> results;

    while (T--) {
        int P, Q, R, S;
        cin >> P >> Q >> R >> S; // Read profits of companies A, B, C, and D

        // Calculate the sum of profits of the other three companies
        int total_other_A = Q + R + S;
        int total_other_B = P + R + S;
        int total_other_C = P + Q + S;
        int total_other_D = P + Q + R;

        // Check for monopoly condition
        if (P > total_other_A || Q > total_other_B || R > total_other_C || S > total_other_D) {
            results.push_back("YES");
        } else {
            results.push_back("NO");
        }
    }

    // Output results
    for (const string &result : results) {
        cout << result << endl;
    }

    return 0;
}

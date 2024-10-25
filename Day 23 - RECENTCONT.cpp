#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T; // Read the number of test cases

    while (T--) {
        int N;
        cin >> N; // Read the number of problems in the current test case
        vector<string> contestCodes(N);
        
        // Read the contest codes into the vector
        for (int i = 0; i < N; i++) {
            cin >> contestCodes[i];
        }

        int countSTART38 = 0, countLTIME108 = 0;

        // Count occurrences of each contest code
        for (const string &code : contestCodes) {
            if (code == "START38") {
                countSTART38++;
            } else if (code == "LTIME108") {
                countLTIME108++;
            }
        }

        // Output the results for the current test case
        cout << countSTART38 << " " << countLTIME108 << endl;
    }

    return 0;
}

#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T; // Read number of test cases
    while (T--) {
        int N;
        cin >> N; // Read the limit for the game
        
        // Determine the winner
        if (N == 1) {
            cout << "ALICE" << endl; // Alice wins when N is 1
        } else {
            cout << "BOB" << endl; // Bob wins for all other values
        }
    }
    return 0;
}


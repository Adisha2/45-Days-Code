
#include <iostream>
#include <vector>

using namespace std;

string isPseudoSorted(int N, vector<int>& A) {
    vector<int> violations;

    // Identify the points of violation
    for (int i = 0; i < N - 1; ++i) {
        if (A[i] > A[i + 1]) {
            violations.push_back(i);
        }
    }

    // If there are no violations, the array is already sorted
    if (violations.empty()) {
        return "YES";
    }

    // If there is more than one violation, we cannot fix it with one swap
    if (violations.size() > 1) {
        return "NO";
    }

    // If there is exactly one violation, check if a swap can sort the array
    int i = violations[0];

    // Try swapping A[i] and A[i + 1]
    swap(A[i], A[i + 1]);

    // Check if the array is sorted after the swap
    for (int j = 0; j < N - 1; ++j) {
        if (A[j] > A[j + 1]) {
            return "NO";
        }
    }

    return "YES";
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<int> A(N);
        for (int i = 0; i < N; ++i) {
            cin >> A[i];
        }
        cout << isPseudoSorted(N, A) << endl;
    }
    return 0;
}

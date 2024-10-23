#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int H, X, Y;
        cin >> H >> X >> Y;

        // Calculate attacks needed using only normal attacks
        int normal_attacks = (H + X - 1) / X;

        // Calculate attacks needed using the special attack first
        int remaining_health = H - Y;
        int special_attacks = 1; // For the special attack

        if (remaining_health > 0) {
            special_attacks += (remaining_health + X - 1) / X;
        }

        // Get the minimum attacks needed
        int min_attacks_needed = min(normal_attacks, special_attacks);
        cout << min_attacks_needed << endl;
    }

    return 0;
}

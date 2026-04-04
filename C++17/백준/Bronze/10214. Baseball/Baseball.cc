#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int y_score_sum = 0, k_score_sum = 0;
    
        for (int i = 0; i < 9; i++) {
    
            int y_score = 0, k_score = 0;
            cin >> y_score >> k_score;

            y_score_sum += y_score;
            k_score_sum += k_score;
        }

        if (k_score_sum > y_score_sum) {
            cout << "Korea\n";
        } else if (y_score_sum > k_score_sum) {
            cout << "Yonsei\n";
        } else {
            cout << "Draw\n";
        }
    }
    return 0;
}
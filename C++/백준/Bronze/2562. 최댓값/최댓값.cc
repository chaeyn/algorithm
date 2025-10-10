#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int maxVal = -1;
    int idx = 0;

    for (int i=0; i<9; i++) {
        int a;
        cin >> a;

        if (a > maxVal) {
            maxVal = a;
            idx = i + 1;
        }
    }

    cout << maxVal << "\n" << idx;

    return 0;
}
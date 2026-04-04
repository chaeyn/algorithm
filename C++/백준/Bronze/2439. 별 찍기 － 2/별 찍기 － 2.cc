#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; i ++) {
        for (int j = 1; j < n - i; j++) {
            cout << " ";
        }
        for (int k = 0; k <= i; k++) {
            cout << "*";
        }
        cout << "\n";
    }
}
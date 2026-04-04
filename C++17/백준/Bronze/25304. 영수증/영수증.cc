#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int total, n, sum = 0;
    cin >> total >> n;

    for (int i = 0; i < n; i++) {
        int a, b = 0;
        cin >> a >> b;
        sum += a * b;
    }
    if (sum == total) cout << "Yes";
    else cout << "No";
}
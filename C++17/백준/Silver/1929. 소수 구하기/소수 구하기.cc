#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m, n;
    cin >> m >> n;

    for (int i=m; i<=n; i++) {
        bool is_prime = true;

        for (int j=2; j*j<=i; j++) {
            if (i%j==0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime && i > 1) {
            cout << i << "\n";
        }
    }

    return 0;
}
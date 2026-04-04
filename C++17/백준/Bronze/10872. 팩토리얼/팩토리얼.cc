#include <bits/stdc++.h>
using namespace std;

int fac(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * fac(n-1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n = 0;
    cin >> n;

    cout << fac(n);

    return 0;
}
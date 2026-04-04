#include <bits/stdc++.h>
using namespace std;

int fac(int n) {
    if (n==1) return n;
    else return fac(n) * fac(n-1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i=n; i>0; i--) cout << i << "\n";

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
    int c;
    while (b!=0) {
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    for (int i=0; i<t; i++) {
        int a, b;
        cin >> a >> b;
        cout << lcm(a, b) << '\n';
    }

    return 0;
}
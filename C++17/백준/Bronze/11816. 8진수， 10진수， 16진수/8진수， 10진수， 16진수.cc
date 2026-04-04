#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string n;
    cin >> n;

    if (n.length() > 1) {
        if (n.substr(0, 2) == "0x") {
            cout << stoi(n, nullptr, 16);
        } else if (n.substr(0, 1) == "0") {
            cout << stoi(n, nullptr, 8);
        } else {
            cout << n;
        }
    }

    return 0;
}
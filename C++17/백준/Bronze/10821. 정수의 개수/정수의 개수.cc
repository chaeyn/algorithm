#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int cnt = 1;

    for (char c : s) {
        if (c == ',') cnt++;
    }

    cout << cnt;

    return 0;
}

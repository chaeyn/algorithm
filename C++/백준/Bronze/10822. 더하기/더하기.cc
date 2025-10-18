#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    stringstream ss(s);
    string t;
    int sum = 0;

    while (getline(ss, t, ',')) {
        sum += stoi(t);
    }

    cout << sum;

    return 0;
}

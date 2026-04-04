#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s = "";
    string line;

    // 여러 줄 읽어서 연결
    while (getline(cin, line)) {
        s += line;
    }

    for (int i=0; i<s.length(); i++) {
        if (s[i] == ',') {
            s[i] = ' ';
        }
    }

    istringstream iss(s);
    long long num;
    long long sum = 0;

    while (iss >> num) {
        sum += num;
    }

    cout << sum;

    return 0;
}
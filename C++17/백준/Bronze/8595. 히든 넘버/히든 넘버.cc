#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    string s;
    cin >> s;

    long long sum = 0;
    int i = 0;

    while (i < n) {
        if (isdigit(s[i])) {
            long long num = 0;
            while (i < n && isdigit(s[i])) {
                num = num * 10 + (s[i] - '0');
                i++;
            }
            sum += num;
        } else {
            i++;
        }
    }

    cout << sum;

    return 0;
}
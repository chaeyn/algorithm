#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        if (n%2==1) {
            cout << "koosaga\n";
        } else {
            cout << "cubelover\n";
        }
    }

    return 0;
}
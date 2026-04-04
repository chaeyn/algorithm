#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x, res;
    cin >> n;

    deque<int> d;
    for (int i=0; i<n; i++) {
        int co;
        cin >> co;

        switch (co) {
            case 1:
                cin >> x;
                d.push_front(x);
                break;
            case 2:
                cin >> x;
                d.push_back(x);
                break;
            case 3:
                if (d.size()>0) {
                    res = d.front();
                    d.pop_front();
                    cout << res << '\n';
                } else {
                    cout << -1 << '\n';
                }
                break;
            case 4:
                if (d.size()>0) {
                    res = d.back();
                    d.pop_back();
                    cout << res << '\n';
                } else {
                    cout << -1 << '\n';
                }
                break;
            case 5:
                cout << d.size() << '\n';
                break;
            case 6:
                if (d.size()>0) {
                    cout << 0 << '\n';
                } else {
                    cout << 1 << '\n';
                }
                break;
            case 7:
                if (d.size()>0) {
                    cout << d.front() << '\n';
                } else {
                    cout << -1 << '\n';
                }
                break;
            case 8:
                if (d.size()>0) {
                    cout << d.back() << '\n';
                } else {
                    cout << -1 << '\n';
                }
                break;
        }
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    stack<int> stk;
    int n;
    cin >> n;

    int co;
    while (n--) {
        cin >> co;
        switch (co) {
            case 1:
                int x;
                cin >> x;
                stk.push(x);
                break;
            case 2:
                if (!stk.empty()) {
                    cout << stk.top() << '\n';
                    stk.pop();
                } else {
                    cout << -1 << '\n';
                }
                break;
            case 3:
                cout << stk.size() << '\n';
                break;
            case 4:
                if (stk.empty()) cout << 1 << '\n';
                else cout << 0 << '\n';
                break;
            case 5:
                if (!stk.empty()) cout << stk.top() << '\n';
                else cout << -1 << '\n';
                break;
            default: cout << -1;
                break;
        }
    }

    return 0;
}
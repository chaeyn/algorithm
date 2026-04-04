#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    cin.ignore(); // \n 제거, 버퍼 빔

    for (int i=1; i<=n; i++) {
        string s;
        getline(cin, s);

        stringstream ss(s);
        string t;
        stack<string> stk;

        while (getline(ss, t, ' ')) stk.push(t);

        cout << "Case #" << i << ": ";

        while (not stk.empty()) {
            cout << stk.top();
            stk.pop();
            if (!stk.empty()) cout << ' ';
        }
        cout << "\n";
    }


    return 0;
}

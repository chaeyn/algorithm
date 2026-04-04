#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    queue<int> q;
    int n;
    cin >> n;


    string co;
    while (n--) {
        cin >> co;

        if (co == "push") {
            int x;
            cin >> x;
            q.push(x);
        } else if (co == "pop") {
            if (q.empty()) {
                cout << -1 << '\n';
            } else {
                int pop = q.front();
                q.pop();
                cout << pop << '\n';
            }
        } else if (co == "size") {
            cout << q.size() << '\n';
        } else if (co == "empty") {
            if (q.empty()) cout << 1 << '\n';
            else cout << 0 << '\n';
        } else if (co == "front") {
            if (q.empty()) {
                cout << -1 << '\n';
            } else {
                int front = q.front();
                if (front) cout << front << '\n';
            }
        } else if (co == "back") {
            if (q.empty()) {
                cout << -1 << '\n';
            } else {
                int back = q.back();
                if (back) cout << q.back() << '\n';
            }
        }
    }

    return 0;
}
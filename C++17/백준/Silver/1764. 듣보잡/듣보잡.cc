#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    set<string> hear;
    vector<string> see;

    for (int i=0; i<n; i++) {
        string not_hear;
        cin >> not_hear;
        hear.insert(not_hear);
    }

    for (int i=0; i<m; i++) {
        string not_see;
        cin >> not_see;
        see.push_back(not_see);
    }

    vector<string> res;
    for (const string & j : see) {
       if (hear.find(j) != hear.end()) {
           res.push_back(j);
       }
    }

    sort(res.begin(), res.end());

    cout << res.size() << '\n';
    for (const string & s : res) {
        cout << s << '\n';
    }

    return 0;
}
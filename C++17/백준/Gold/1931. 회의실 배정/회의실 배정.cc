#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<pair<int, int>> v(n);

    for (int i=0; i<n; i++) {
        int start, end;
        cin >> start >> end;
        v[i] = {end, start};
    }

    sort(v.begin(), v.end());

    int cnt = 0;
    int end_time = 0;

    for (int i=0; i<n; i++) {
        int end = v[i].first;
        int start = v[i].second;

        if (start >= end_time) {
            cnt++;
            end_time = end;
        }
    }

    cout << cnt;

    return 0;
}
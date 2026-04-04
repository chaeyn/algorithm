#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, t, cnt = 0;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];

    cin >> t;

    for (int i = 0; i < n; i++) if (v[i] == t) cnt++;
    cout << cnt;

    return 0;
}
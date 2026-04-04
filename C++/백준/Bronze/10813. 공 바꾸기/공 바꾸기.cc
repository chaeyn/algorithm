#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<int> v(n+1);
    for (int i=1; i<=n; i++) v[i] = i;

    for (int a=0; a<m; a++){
        int i, j;
        cin >> i >> j;
        swap(v[i], v[j]);
    }

    for (int i=1; i<=n; i++) {
        cout << v[i] << " ";
    }

    return 0;
}
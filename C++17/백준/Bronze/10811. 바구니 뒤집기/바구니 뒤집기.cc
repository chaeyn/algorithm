#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<int> v(n+1);
    for (int i=0; i<=n; i++) v[i] = i;

    for (int i=0; i<m; i++) {
        int a, b, temp = 0;
        cin >> a >> b;
        while (a < b) {
            temp = v[a];
            v[a] = v[b];
            v[b] = temp;
            a++; b--;
        }
    }

    for (int i=1; i<=n; i++) cout << v[i] << " ";

    return 0;
}
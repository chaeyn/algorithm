#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<int> v(n, 0); // 크기 n, 초기값 0

    for (int a=0; a<m; a++) {
        int i, j, k;
        cin >> i >> j >> k;

        for (int b=i; b<=j; b++) {
            v[b-1] = k;
        }
    }

    for (int x : v) {
        cout << x << " ";
    }

    return 0;
}
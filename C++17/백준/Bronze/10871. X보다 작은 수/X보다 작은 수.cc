#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    vector<int> v;
    for (int i=0; i<n; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }

    for (int i=0; i<n; i++) if (v[i] < x) cout << v[i] << " ";

    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> v;
    for (int i=0; i<n; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }

    cout << *min_element(v.begin(), v.end()) << " " << *max_element(v.begin(), v.end());

    return 0;
}
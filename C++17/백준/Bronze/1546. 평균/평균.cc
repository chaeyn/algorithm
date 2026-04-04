#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n = 0;
    float max, avg = 0;
    cin >> n;

    vector<float> v(n+1, 0);
    for (int i=0; i<n; i++) {
        float s;
        cin >> s;
        v[i] = s;
        if (v[i] >= max) max = v[i];
    }
    for (int i=0; i<n; i++) {
        avg += (v[i]/max)*100;
    }

    float cnt = n;

    cout << avg/cnt;

    return 0;
}
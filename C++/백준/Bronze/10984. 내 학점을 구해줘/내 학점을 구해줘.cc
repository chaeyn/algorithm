#include <iostream>
#include <vector>
using namespace std;

int fac(int n) {
    if (n==1) return n;
    else return fac(n) * fac(n-1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 0;
    cin >> t;

    for (int i=0; i<t; i++) {
        int n = 0;
        cin >> n;
        float ccnt = 0;
        float gsum = 0;
        for (int j=0; j<n; j++) {
            int c;
            float g;
            cin >> c >> g;
            ccnt += c;
            gsum += c*g;
        }
        float avgg = gsum / ccnt;
        cout.precision(2);
        cout << ccnt << " " << avgg << "\n";
    }

    return 0;
}
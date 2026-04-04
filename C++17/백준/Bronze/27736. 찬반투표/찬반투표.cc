#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 0, p = 0, r = 0, n = 0;
    cin >> t;

    for (int i=0; i<t; i++) {
        int a = 0;
        cin >> a;
        if (a==0) r++;
        if (a==1) p++;
        if (a==-1) n++;
    }

    if (r*2 >= t) cout << "INVALID";
    else if (p>n) cout << "APPROVED";
    else if (p<=n) cout << "REJECTED";

    return 0;
}
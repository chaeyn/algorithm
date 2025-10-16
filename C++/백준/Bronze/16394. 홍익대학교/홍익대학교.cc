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

    int n;
    cin >> n;

    cout << n - 1946;

    return 0;
}
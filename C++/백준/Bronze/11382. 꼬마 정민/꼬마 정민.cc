#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // 10^9 초과 -> long long
    long long a, b, c;
    cin >> a >> b >> c;
    cout << a + b + c;

    return 0;
}
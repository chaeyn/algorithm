#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a = 300, b = 60, c = 10;
    int a_cnt = 0, b_cnt = 0, c_cnt = 0;

    while (n > 0) {
        if (n - a >= 0) {
            n -= a;
            a_cnt++;
        } else if (n - b >= 0) {
            n -= b;
            b_cnt++;
        } else if (n - c >= 0) {
            n -= c;
            c_cnt++;
        } else {
            cout << -1;
            return 0;
        }
    }

    cout << a_cnt << " " << b_cnt << " " << c_cnt;
    return 0;
}
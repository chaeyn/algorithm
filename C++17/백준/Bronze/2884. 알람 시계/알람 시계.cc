#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int h, m;
    cin >> h >> m;

    if (m - 45 < 0) {
        h--;
        if (h < 0) {
            h = 23;
        }
        m += 60 - 45;
    } else {
        m -= 45;
    }

    cout << h << " " << m;

    return 0;
}
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b;
    cin >> a >> b;

    cout << a * (b % 10) << "\n"; // 일의 자리
    cout << a * ((b / 10) % 10) << "\n"; // 십의 자리
    cout << a * (b / 100) << "\n"; // 백의 자리
    cout << a * b << "\n";

    return 0;
}
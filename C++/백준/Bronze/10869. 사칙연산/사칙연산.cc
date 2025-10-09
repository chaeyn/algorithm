#include <iostream>
using namespace std;

int main() {
    // 빠른 입출력
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b;
    cin >> a >> b;
    cout << a + b << "\n";
    cout << a - b << "\n";
    cout << a * b << "\n";
    cout << a / b << "\n";
    cout << a % b << "\n";
    return 0;
}
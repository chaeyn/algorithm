#include <iostream>
using namespace std;

int main() {
    // 빠른 입출력
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double a, b;
    cin >> a >> b;
    cout.precision(15); // 유효숫자 15자리 출력
    cout << a / b << "\n";
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b;
    while (cin >> a >> b) { // EOF까지 입력 받기
        cout << a + b << "\n";
    }
}
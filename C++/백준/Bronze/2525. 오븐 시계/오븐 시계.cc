#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int h, m, c;
    cin >> h >> m >> c;

    m += c;
    h += m / 60; // 분 넘쳤으면 시간에 더하기
    m %= 60; // 넘친 시간은 60 미만으로
    h %= 24; // 24 넘으면 다음날로

    cout << h << " " << m;

    return 0;
}
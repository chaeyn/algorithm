#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    int cnt = 0;

    for (int i=1; i<n; i++) {
        string num = to_string(i);
        if (num.find("50") != string::npos) cnt++;
    }

    cout << n + cnt;

    return 0;
}
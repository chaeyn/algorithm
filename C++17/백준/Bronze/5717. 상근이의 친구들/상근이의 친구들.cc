#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    while (true) {
        int m, f = 0;
        cin >> m >> f;
        if(m+f==0) break;
        cout << m+f << "\n";
    }

    return 0;
}
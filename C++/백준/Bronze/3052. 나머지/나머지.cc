#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    set<int> s;

    for (int i=0; i<10; i++) {
        int n = 0;
        cin >> n;
        s.insert(n % 42);
   }

    cout << s.size();

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    if (n==0) {
        cout << 0;
        return 0;
    }

    vector<int> opinions(n);
    for (int i=0; i<n; i++) {
        cin >> opinions[i];
    }

    sort(opinions.begin(), opinions.end());

    int exclude = round(n * 0.15);

    double sum = 0;
    int cnt = 0;

    // 절사평균 제외할 값 앞/뒤 제외
    for (int i=exclude; i<n-exclude; i++) {
        sum += opinions[i];
        cnt++;
    }

    cout << round(sum/cnt);

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    stringstream ss(s);
    string t;
    vector<int> v1;

    while (getline(ss, t, ',')) {
        v1.push_back(stoi(t));
    }

    for (int i=0; i<k; i++) {
        vector<int> v2;
        for (int j=0; j<v1.size() - 1; j++) {
            v2.push_back(v1[j+1] - v1[j]);
        }
        v1 = v2;
    }

    for (int i=0; i<v1.size(); i++) {
        cout << v1[i];
        if (i < v1.size()-1) cout << ','; // 마지막은 쉼표 없이 출력
    }

    return 0;
}
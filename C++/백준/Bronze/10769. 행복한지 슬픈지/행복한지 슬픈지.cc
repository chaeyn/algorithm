#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    getline(cin, s); // 공백 포함 전체 줄 읽기

    int happy = 0, sad = 0;

    for (int i=0; i<s.length(); i++) {
        if (s[i] == ':' && s[i+1] == '-' && s[i+2] == ')') {
            happy++;
        } else if (s[i] == ':' && s[i+1] == '-' && s[i+2] == '(') {
            sad++;
        }
    }

    if (happy + sad == 0) {
        cout << "none";
    } else if (happy == sad) {
        cout << "unsure";
    } else if (happy > sad) {
        cout << "happy";
    } else if (sad > happy) {
        cout << "sad";
    }

    return 0;
}
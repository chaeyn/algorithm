#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string isbn;
    cin >> isbn;

    int star_pos = -1;
    int sum = 0;

    for (int i=0; i<13; i++) {
        if (isbn[i] == '*') {
            star_pos = i;
        } else {
            int digit = isbn[i] - '0';
            if (i%2==0) {
                sum += digit * 1;
            } else {
                sum += digit * 3;
            }
        }
    }

    for (int x=0; x<=9; x++) {
        int weight;
        if (star_pos%2==0) {
            weight = 1;
        }else {
            weight = 3;
        }

        int total = sum + x * weight;

        if (total % 10 == 0) {
            cout << x;
            return 0;
        }
    }




    return 0;
}
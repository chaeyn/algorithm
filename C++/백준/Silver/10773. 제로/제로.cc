#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int capacity;
    cin >> capacity;

    vector<int> array(capacity);
    int top = -1;

    for (int i=0; i<capacity; i++) {
        int n;
        cin >> n;
        if (n==0) {
            if (top >=0) top--;
        } else {
            top++;
            if (top < capacity) array[top] = n;
        }
    }

    int sum = 0;
    for (int i=0; i<=top; i++) {
        sum += array[i];
    }

    cout << sum;

    return 0;
}
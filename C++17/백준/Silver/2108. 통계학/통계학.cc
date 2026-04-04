#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> nums(n);
    long long sum = 0;

    for (int i=0; i<n; i++) {
        cin >> nums[i];
        sum += nums[i];
    }

    sort(nums.begin(), nums.end());

    // 산술평균
    double avg = (double)sum / n;
    cout << (int)round(avg) << '\n';

    // 중앙값
    cout << nums[n/2] << "\n";

    // 최빈값
    map<int, int> freq;

    for (int i=0; i<n; i++) {
        freq[nums[i]]++;
    }

    int maxFreq = 0;
    for (int i=0; i<n; i++) {
        if (freq[nums[i]] > maxFreq) {
            maxFreq = freq[nums[i]];
        }
    }

    vector<int> modes;
    for (int i=0; i<n; i++) {
        int num = nums[i];
        if (freq[num] == maxFreq) {
            if (modes.empty() || modes.back() != num) {
                modes.push_back(num);
            }
        }
    }

    if (modes.size() == 1) cout << modes[0] << '\n';
    else cout << modes[1] << '\n';

    // 범위
    cout << nums[n-1] - nums[0] << '\n';

    return 0;
}
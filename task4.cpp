#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll maxSubarrayNoMoreThanK(const vector<ll>& arr, ll K) {
    multiset<ll> prefixes;
    prefixes.insert(0);
    ll best = LLONG_MIN, sum = 0;
    for (ll x : arr) {
        sum += x;
        // we need a prefix >= sum - K
        auto it = prefixes.lower_bound(sum - K);
        if (it != prefixes.end()) {
            best = max(best, sum - *it);
        }
        prefixes.insert(sum);
    }
    return best;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    ll K;
    cin >> n >> m >> K;
    vector<vector<ll>> A(n, vector<ll>(m));
    for(int i = 0; i < n; i++)
      for(int j = 0; j < m; j++)
        cin >> A[i][j];

    ll answer = LLONG_MIN;
    // fix left and right column boundaries
    for(int left = 0; left < m; left++){
        vector<ll> rowSum(n, 0);
        for(int right = left; right < m; right++){
            for(int i = 0; i < n; i++){
                rowSum[i] += A[i][right];
            }
            ll best1D = maxSubarrayNoMoreThanK(rowSum, K);
            answer = max(answer, best1D);
        }
    }

    if(answer < LLONG_MIN/2) 
        cout << -1 << "\n";
    else 
        cout << answer << "\n";

    return 0;
}

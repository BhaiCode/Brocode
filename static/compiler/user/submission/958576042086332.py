#include <bits/stdc++.h>
using namespace std;

const int MAXK = 100, MAXT = 100, MAXN = 100000, MAXA = 1E9;
int cnt[110], n, k;
void solve() {
    memset(cnt, 0, sizeof(cnt) );
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        x %= k;
        cnt[x]++;
    }
    int ans = 0;
    ans += min(1, cnt[0]);
    for (int i = 1; i < k/2 + k%2; i++) {
        ans += max(cnt[i], cnt[k - i]);
    }
    if (k % 2 == 0) {
        ans += min(1, cnt[k/2]);
    }
    cout<<ans<<endl;
}

int main() {
    int cases = 1;
    for (int i = 0; i < cases; i++) {
        solve();
    }
    return 0;
}
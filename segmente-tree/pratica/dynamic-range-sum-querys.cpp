#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define optimize ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define INF 100000010
#define ALL(x) x.begin(), x.end()
#define UNIQUE(c) (c).resize(unique(ALL(c)) - (c).begin())
#define REP(i, a, b) for(int i = (a); i <= (b); i++)
#define POS(n, x) (lower_bound(ALL(n), x) - (n).begin())
#define ll long long
#define ld long double
#define pii pair<int,int>
#define vi vector<int>
#define vii vector<pii>
#define os_type int
#define PB push_back
#define EB emplace_back
#define MOD 1000000007
#define PRIME 101 
#define MAXN 210000
#define MAXL 23
#define endl '\n'
 
using namespace std;
using namespace __gnu_pbds;
 
#define ordered_set tree<os_type, null_type,less<os_type>, rb_tree_tag,tree_order_statistics_node_update>

ll treee[4 * MAXN];
ll arr[MAXN];

 
void update(int pos, int i, int j, int x, ll val){
	int esq = 2*pos;
	int dir = 2*pos + 1;
	int mid = (i+j)/2;
 
	treee[pos] += val;
 
	if(i == j) return;
	if(x <= mid) update(esq, i, mid, x, val);
	else update(dir, mid+1, j, x, val);
}
 
ll query(int pos, int i, int j, int l, int r){
	int esq = 2*pos;
	int dir = 2*pos + 1;
	int mid = (i+j)/2;
 
	if(i > r || j < l) return 0;
	if(i >= l && j <= r) return treee[pos];
	else return query(esq, i, mid, l, r) + query(dir, mid+1, j, l, r);
}

int main(){
    optimize;
    int n, q;
    cin >> n >> q;

    for (int i = 0; i<n; i++){
        ll v;
        cin >> v;
        update(1, 0, n-1, i, v);
        arr[i] = v;
    }

    for (int j = 0; j<q; j++){
        int a, b;
        cin >> a >> b;
        if (a==1){
            ll c;
            cin >> c;
            update(1, 0, n-1, b-1, c-arr[b-1]);
        }
        else {
            int c;
            cin >> c;
            cout << query(1, 0, n-1, b-1, c-1) << endl;
        }
    }

}
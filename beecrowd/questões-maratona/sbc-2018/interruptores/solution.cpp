//
// Created by Luis on 30/08/2023.
//
//Template By eduardocesb
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define optimize ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define INF 1000000010
#define INFLL 1000000000000000010LL
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
#define MAXN 1010101
#define MAXL 23
#define EPS 1e-9
#define endl '\n'

using namespace std;
using namespace __gnu_pbds;

#define ordered_set tree<os_type, null_type,less<os_type>, rb_tree_tag,tree_order_statistics_node_update>


int main(int argc, char** argv)
{
    optimize;
    bitset<1000> bt;
    int n ,m; cin >> n >> m;
    int l; cin >> l;
    while(l--){
        int pos; cin >> pos;
        bt.flip(pos-1);
    }
    vector<int>inter [n];
    for(int i =0;i < n;i++){
        int quant; cin >> quant;
        for(int j =0;j < quant;j++){
            int lamp;cin >> lamp;
            inter[i].EB(lamp - 1);
        }
    }
    bitset<1000> aux = bt;
    for(int i =0; i < 2 * n;i++ ){
        int atual = i % n;
        for(int x : inter[atual]){
                aux.flip(x);
            }
        if(aux.count() == 0) {
            cout << i + 1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}


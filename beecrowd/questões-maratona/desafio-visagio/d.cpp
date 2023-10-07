//
// Created by Luis on 07/10/2023.
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
 
 
int main(int argc, char **argv) {
    optimize;
    int n, b;
    cin >> n >> b;
    bitset<10010> meios[10];
    int custo[10];
    vector<int> ordem;
    for (int i = 0; i < n; i++) {
        ordem.EB(i);
        cin >> custo[i];
        int m;
        cin >> m;
        while (m--) {
            int pessoa;
            cin >> pessoa;
            meios[i].set(pessoa);
        }
    }
    ll resposta = 0;
    do {
        bitset<10010> ans;
        int valor = 0;
        for (int i = 0; i < n; i++) {
            if (valor + custo[ordem[i]] > b) {
                break;
            }
            valor+=custo[ordem[i]];
            ans |= meios[ordem[i]];
        }
        resposta = max(resposta, (ll) ans.count());
 
    } while (next_permutation(ALL(ordem)));
 
    cout << resposta << endl;
 
    return 0;
}
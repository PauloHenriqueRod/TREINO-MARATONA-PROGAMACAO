#include <bits/stdc++.h>
#include <string>
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
#define MAXN 101010
#define MAXL 23
#define endl '\n'

using namespace std;

#define ordered_set tree<os_type, null_type,less<os_type>, rb_tree_tag,tree_order_statistics_node_update>

int CAPACIDADE, N;
int peso[MAXN], valor[MAXN];

map<pii, int> memo;


int solve(int i, int c){
    if (i >= N)
        return 0;
    if (c<=0){
        return 0;
    }

    if (memo.find({i,c}) != memo.end())
        return memo[{i, c}];

    int nao_pega = solve(i+1, c);
    int pega = 0;
    
    if (peso[i] <= c)
        pega = valor[i] + solve(i+1, peso[i]);
    
    return memo[{i,c}]  = max(pega, nao_pega);
}


int main(){
    optimize;
    cin >> CAPACIDADE >> N;

    for (int i = 0; i<N; i++){
        cin >> peso[i] >> valor[i];
}
}

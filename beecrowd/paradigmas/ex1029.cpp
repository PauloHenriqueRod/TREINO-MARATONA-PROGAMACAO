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

int dp[101010];
int dp_cals[101010];

int fibo(int n){
    if(n == 0 || n == 1)
        return n;
    if(dp[n]!=0)
        return dp[n];
    return dp[n] = fibo(n-1) + fibo(n-2);
}

int fibo_calls(int n){
    if(n == 0 || n == 1)
        return 0;
    if(dp_cals[n] != 0)
        return dp_cals[n];
    return dp_cals[n] =  fibo_calls(n-1) + fibo_calls(n-2) + 2;
}

int main(){
    int a;
    int x;
    cin >> x;
    for(int i = 0; i<x; i++){
        cin >> a;
        cout << "fib(" << a << ") = " << fibo_calls(a) << " calls = " << fibo(a) << endl;
    }
}
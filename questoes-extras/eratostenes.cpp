#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define optimize ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define INF 0x3f3f3f3f
#define INFLL 0x3f3f3f3f3f3f3f3fLL
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
 
/*
 
 
a * b = N
a <= b
 
*/
 
 
// O(sqrt(N))
// bool eh_primo(ll N)
// {
//  if (N == 1) return false;
 
//  // (1, N)
//  for (ll i = 2; i * i <= N; i++)
//      if (N % i == 0)
//          return false;
    
//  return true;
// }
 
// Crivo de Eratóstenes
 
// O(N * log(N))
 
vector<int> primos;
 
vector<bool> crivo(int N)
{
    vector<bool> eh_primo(N + 1, true);
 
    eh_primo[0] = eh_primo[1] = false;
 
    // O(N * log N)
    for (ll i = 2; i <= N; i++)
    {
        if (!eh_primo[i]) continue;
 
        // i é primo
        primos.push_back(i);
 
        for (ll j = i * i; j <= N; j += i)
            eh_primo[j] = false;
    }
 
    return eh_primo;
}
 
int main(int argc, char** argv)
{
    optimize;
 
    ll N;
 
    cin >> N;
 
    auto eh_primo = crivo(N);
 
    // O(N)
    for (int i = 2; i <= N; i++)
        if (eh_primo[i])
            cout << i << " ";
    
    cout << endl;
 
    return 0;
}
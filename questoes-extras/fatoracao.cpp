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
#define pii pair<ll,int>
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
 
// 10^12
 
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
 
vector<ll> primos;
 
vector<int> crivo(int N)
{
    vector<int> eh_primo(N + 1, 1);
 
    eh_primo[0] = eh_primo[1] = 0;
 
    int pos = 1;
 
    // O(N * log N)
    for (ll i = 2; i <= N; i++)
    {
        if (!eh_primo[i]) continue;
 
        eh_primo[i] = pos++;
 
        // i é primo
        primos.push_back(i);
 
        for (ll j = i * i; j <= N; j += i)
            eh_primo[j] = 0;
    }
 
    return eh_primo;
}
 
// a * b = N
// a <= b
// a <= sqrt(N)
// b >= sqrt(N)
// 2 * sqrt(N)
 
vector<ll> get_divisores(ll N)
{
    vector<ll> divisores;
    
    for (ll i = 1; i * i <= N; i++)
    {
        if (N % i != 0) continue;
 
        divisores.push_back(i);
 
        if (i * i != N)
            divisores.push_back(N / i);
    }
 
    return divisores;
}
 
vii fatora(ll N)
{
    vii ans;
 
    // O(sqrt(N))
    for (ll i = 2; i * i <= N; i++)
    {
        if (N % i != 0) continue;
 
        int qtd = 0;
 
        while (N % i == 0)
        {
            qtd++;
            N /= i;
        }
 
        ans.push_back({i, qtd});
    }
 
    if (N != 1)
        ans.push_back({N, 1});
 
    return ans;
}
 
 
int main(int argc, char** argv)
{
    optimize;
 
    ll N;
 
    auto pos = crivo(1e7);
 
    cin >> N;
 
    while (N--)
    {
        int P;
        cin >> P;
 
        cout << pos[P] << endl; 
    }
 
    return 0;
}
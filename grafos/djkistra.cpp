#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
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
using namespace __gnu_pbds;

#define ordered_set tree<os_type, null_type,less<os_type>, rb_tree_tag,tree_order_statistics_node_update>

 
int N, M;
 
// grafo[u] = [(v, custo), (v, custo), (v, custo), ...]
 
vector<pii> grafo[MAXN];
 
vector<int> pai(MAXN, -1);

int Dijkstra(int origem)
{
    // fila.top() = (distancia, vertice)
    priority_queue<pii, vector<pii>, greater<pii>> fila;
 
    vector<int> distancias(N + 10, INT_MAX);
 
    distancias[origem] = 0;
    fila.push({0, origem});
 
    vector<bool> visitados(N + 10, false);
    int teste = 0;
    while (fila.empty() == false)
    {
        auto [dist, atual] = fila.top();
        fila.pop();
 
        if (visitados[atual])
            continue;
 
        visitados[atual] = true;
        int teste = 0;
        for (auto [vizinho, custo] : grafo[atual])
        {
            if (distancias[vizinho] > distancias[atual] + custo)
            {
                distancias[vizinho] = distancias[atual] + custo;
                fila.push({distancias[vizinho], vizinho});
                pai[vizinho] = atual;
                teste += 1;
            }
        }
    }
 
    return teste;
}
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    cin >> N >> M;
 
    for (int i = 0; i < M; i++)
    {
        int u, v, custo;
 
        cin >> u >> v >> custo;
 
        grafo[u].emplace_back(v, custo);
        // grafo[v].push_back({u, custo});
    }
 
    int distancias = Dijkstra(0);
 
    cout << distancias << endl;
 
}
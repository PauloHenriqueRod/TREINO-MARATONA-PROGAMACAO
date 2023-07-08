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
#define MAXN 101010
#define MAXL 23
#define endl '\n'
 
using namespace std;
using namespace __gnu_pbds;
 
#define ordered_set tree<os_type, null_type,less<os_type>, rb_tree_tag,tree_order_statistics_node_update>
 
/*
BFS: Fila => queue 
DFS: Pilha => stack
*/
 
vector<int> grafo[MAXN];
 
int N, M;
 
void busca(int origem, vector<bool> &visitados)
{
    stack<int> fila;
 
    fila.push(origem);
 
    while (fila.size() > 0)
    {
        int atual = fila.top();
 
        fila.pop();
 
        if (visitados[atual] == true)
        {
            continue;
        }
 
        visitados[atual] = true;
 
        for (auto proximo : grafo[atual])
        {
            if (visitados[proximo] == false)
            {
                fila.push(proximo);
            }
        }
    }

}
 
bool solve()
{

    for (int i = 1; i <= N; i++)
    {
        vector<bool> visitados(N + 1, 0);
 
        busca(i, visitados);
 
        for (int j = 1; j <= N; j++)
            if (visitados[j] == false)
            {
                return false;
            }
    }
    
    return true;
}
 
int main(int argc, char** argv)
{
    optimize;
 
    while ((cin >> N >> M) && (N != 0 || M != 0))
    {
        for (int i = 0; i <= N; i++)
            grafo[i].clear();
 
        
        for (int i = 0; i < M; i++)
        {
            int v, w, p;
    
            cin >> v >> w >> p;
    
            if (p == 1)
            {
                grafo[v].push_back(w);
            }
            else
            {
                grafo[v].push_back(w);
                grafo[w].push_back(v);
            }
        }
 
        cout << solve() << endl;
    }
    
    return 0;
}
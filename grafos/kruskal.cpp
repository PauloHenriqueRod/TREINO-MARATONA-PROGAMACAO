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

struct Aresta{
    int u, v, c;

    Aresta() {}

    Aresta(int origem, int destino, int custo){
        this->u = origem;    
        this->v = destino;
        this->c = custo;
    }

    bool operator<(const Aresta &outro) const{
        return c < outro.c;
    }
};


struct Grafo
{
    vector<Aresta> arestas;
    vector<int> pai;
 
    Grafo(int N)
    {
        pai.resize(N+1);
        for (int i = 0; i<=N; i++){
            pai[i] = i;
        }
    }

    void join(int u, int v){
        u = find(u);
        v = find(v);
        pai[v] = u;
    }

    int find(int i){
        if (pai[i] == i)
            return i;
        return find(i);
    }
    
 
    void addAresta(int origem, int destino, int custo)
    {
        arestas.emplace_back(origem, destino, custo);
    }

    bool tem_ciclo(int x, int n){
        return find(x) == find(n);
    }
 
    vector<Aresta> kruskal(){
        sort(ALL(arestas));
        vector<Aresta> mst;
        
        for (auto &aresta: arestas){
            int origem = aresta.u;
            int destino = aresta.v;
            int custo = aresta.c;

            if (!tem_ciclo(origem, destino)){
                join (origem, destino);
                mst.push_back(aresta);
        }
        }
        return mst;
    }
};

int main(){
    optimize;

    while (true){
        cin >> N >> M;
        if (N == 0 && M == 0){
            break;
        }
        int u, v, c;
        int custo_total = 0;
        Grafo g(N);

        for (int i = 0; i<M; i++){
            cin >> u >> v >> c;

            g.addAresta(u, v, c);
            
            custo_total += c;
        }
        cout << custo_total << endl;
    }
}
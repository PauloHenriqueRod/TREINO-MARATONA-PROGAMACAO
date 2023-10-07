#include <bits/stdc++.h>
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

vector<vector<int>> doacoes(1495, vector<int>(13, 0));

int main() {
    int N;
    cin >> N;
    int A = 2006;
    for(int i = 0; i < N; i++){
        int ano;
        int mes;
        int val;
        cin >> ano >> mes >> val;
        doacoes[ano - A][mes - 1] += val;
        doacoes[ano - A][12] += val;
    }

    int ano, mes;
    cin >> ano >> mes;
    ano = ano - A;
    ll total = 0;
    for(int i = 0; i < A; i++){
        total += doacoes[i][12];
    }
    for(int j = 0; j < mes; j++){
        total += doacoes[ano][j];
    }

    cout << total << endl;

    return 0;
}
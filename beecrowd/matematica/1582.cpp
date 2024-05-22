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


int euclidiano(int a, int b){
    if(b==0)
        return a;
    return euclidiano(b, a%b);
}
int main(){
    int x, y, z;
    while (cin >> x >> y >> z; != EOF){
    if(x > y) swap(x, y);
    if(y>z) swap(y, z);
    if (z*z == y*y + x*x){
        if(euclidiano(x, euclidiano(y, z)==1)){
            cout << "tripla pitagorica primitiva" << endl;
        }
        else{
            cout << "tripla pitagorica" << endl;
        }
    }
    else{
        cout << "tripla" << endl;
    }
    }
}
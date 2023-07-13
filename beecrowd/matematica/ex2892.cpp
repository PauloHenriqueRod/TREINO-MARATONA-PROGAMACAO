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
 

bool mmc_true(int a, int b, int c, int t) {
    int maior;
    if (a >= b && a >= c) {
        maior = a;
    } else if (b >= a && b >= c) {
        maior = b;
    } else {
        maior = c;
    }

    for (int i = maior; i <= t; i += maior) {
        if (i % a == 0 && i % b == 0 && i % c == 0) {
            if (i == t) {
                return true;
            }
            return false;
        }
    }
    return false;
}

int main() {
    while (true) {
        int x, y, z;
        cin >> x >> y >> z;
        if (x == 0 && y == 0 && z == 0) {
            break;
        }

        int inicio = x / (y * z);
        for (int i = inicio; i <= (x / 2); i += inicio) {
            if (mmc_true(y, z, i, x)) {
                std::cout << i << " ";
            }
        }
        cout << x << endl;
    }

    return 0;
}
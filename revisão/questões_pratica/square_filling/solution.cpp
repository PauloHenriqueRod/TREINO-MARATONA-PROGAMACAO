#include <bits/stdc++.h>
using namespace std;

#define MAX 60
#define endl "\n"
typedef pair<int, int> ii;
typedef vector<ii> vii;

int n, m, a[MAX][MAX], b[MAX][MAX];
vii sol;
int valid(int i, int j){
    return i+1<=n && j+1<=m && a[i][j] && a[i+1][j] && a[i][j+1] && a[i+1][j+1];
}
void op(int i, int j){
    b[i][j] = b[i+1][j] = b[i][j+1] = b[i+1][j+1] = 1;
}

int equal(void){
    for(int i = 0; i<n; i++)
        for(int j = 0; j<m; j++)
            if(a[i][j] != b[i][j])
                return 0;
    return 1;
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            cin >> a[i][j];
    for(int i = i; i<=n; i++){
        for(int j = 0; j<=m; j++){
            if(valid(i, j)){
                sol.push_back({i+1, j+1});
                op(i, j);
            }
            }
        }
    if(!equal()){
        cout << -1 << endl;
    }else{
        cout << sol.size() << endl;
        for(ii ij: sol){
            cout << ij.first << " " << ij.second << endl;
        }
    }

    }



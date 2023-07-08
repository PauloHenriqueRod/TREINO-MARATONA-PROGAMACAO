#include <bits/stdc++.h>
#include <vector>

using namespace std;
int main(){
    int n;
    cin >> n;
    for (int i = 0; i<n; i++){
        int esq = 0;
        int dir = 0;
        string cod;
        cin >> cod;
        for (int j = 0; j<n; j++){
            if (cod[j] == '<')
                esq++;
            if (cod[j] == '>')
                dir++;
        }
        if (esq<=dir)
            cout << esq << endl;
        else
            cout << dir << endl;
    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

int main(){
    int x, fator = 0, aux=1;
    cin >> x;
    for (int i=0; i<x; i++){
        if (i==x-1){
            cout << fator << endl; 
        }
        else{
            cout << fator << " ";
        }
        fator += aux;
        aux = fator - aux;
}
    return 0;
}
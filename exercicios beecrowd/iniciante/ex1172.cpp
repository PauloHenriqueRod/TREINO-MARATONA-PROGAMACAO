#include <bits/stdc++.h>

using namespace std;



int main(){
    int vetor[10];
    int a = 10;
    for (int i = 0; i<a; i++){
        cin >> vetor[i];
        if (vetor[i]<=0){
            vetor[i]=1;
        }
    }
    for (int i = 0; i<a; i++){
        cout << "X[" << i << "] = " << vetor[i]<< endl;
    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;


int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int x;
    cin >> x;
    stack<int> pilha;
    multiset<int> valunicos;
    for (int i = 0; i<x; i++){
        string comando;
        cin >> comando;
        if (comando == "PUSH"){
            int y;
            cin >> y;
            pilha.push(y);
            valunicos.insert(y);
            continue;
        }
        if (comando == "POP"){
            if (pilha.empty()){
                cout << "EMPTY" << endl;
            }
            else{
                valunicos.erase(valunicos.find(pilha.top()));
                pilha.pop();
            }
            continue;
        }
        if (comando == "MIN"){
            if (pilha.empty()){
                cout << "EMPTY" << endl;
            }
            else{
                cout << *valunicos.begin() << endl;
            }
            continue;
        }
    }
}
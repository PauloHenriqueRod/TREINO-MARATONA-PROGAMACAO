#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second

typedef pair<long long,long long int> ponto;

long long int e_esquerda(ponto a, ponto b, ponto c){
    long long int det = (b.x-a.x)*(c.y-a.y) - (c.x-a.x)*(b.y-a.y);
    if (det>0) return 1; // c esta a esquerda
    if (det<0) return -1; // c esta a direita
    return 0; // pontos colineares
}

int main(){
    long long int x1, y1, x2, y2, x3, y3, n;
    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        ponto p1 = ponto(x1, y1);
        ponto p2 = ponto(x2, y2);
        ponto p3 = ponto(x3, y3);
        int resp = e_esquerda(p1, p2, p3);
        if(resp == 1){
            cout << "LEFT" << endl;
            continue;
        }
        if(resp == 0){
            cout << "TOUCH" << endl;
            continue;
        }
        cout << "RIGHT" << endl;
    }

}
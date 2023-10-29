#include <bits/stdc++.h>

using namespace std;

#define y first
#define x second

typedef pair<int,int> ponto;

int e_esquerda(ponto a, ponto b, ponto c){
    int det = (b.x-a.x)*(c.y-a.y) - (c.x-a.x)*(b.y-a.y);
    if (det>0) return 1; // c esta a esquerda
    if (det<0) return -1; // c esta a direita
    return 0; // pontos colineares
}

int main(){
    int n, xa, xb;
    cin >> n >> xa >> xb;
    ponto pts[n];
    for (int i = 0; i< n; i++){
        cin >> pts[i].x >> pts[i].y;
    }
    sort(pts, pts+n);
    ponto pa = ponto(0, xa);
    ponto pb = ponto(0, xb);
    int memo[n], ans=0;
    for (int i = 0; i < n; i++) {
        memo[i] = 1;
        for (int j = i-1; j >= 0; j--) 
            if (e_esquerda(pts[i], pa, pts[j]) == 1 && e_esquerda(pb, pts[i], pts[j]) == 1) 
                memo[i] = max(memo[i], memo[j]+1);
        ans = max(ans, memo[i]);
    }
    cout << ans << endl;
}
#include <bits/stdc++.h>

using namespace std;

int mochila_prob(int CAP, int w[], int v[], int n) {
   int capt;

   int M[n + 1][CAP + 1];

   for (int i = 0; i <= n; i++) {
      for (capt = 0; capt <= CAP; capt++) {
        if (i == 0 || capt == 0)
            M[i][capt] = 0;
        else if (w[i - 1] <= capt)
            M[i][capt] = max(v[i - 1] + M[i - 1][capt - w[i - 1]], M[i - 1][capt]);
        else
            M[i][capt] = M[i - 1][capt];
      }
   }
   return M[n][CAP];
}

int main(){
    int n, mcap;
    cin >> n;
    cin >> mcap;
    int pesos[n];
    int valores[n];
    for (int i = 0; i<=n; i++){
        cin >> pesos[i];
        cin >> valores[i];
    }
    int x = mochila_prob(mcap, pesos, valores, n);
    cout << x;
}

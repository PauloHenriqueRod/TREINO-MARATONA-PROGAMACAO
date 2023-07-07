#include <bits/stdc++.h>

using namespace std;

int main(){
    int x;
    cin >> x;
    for (int i = 0; i<x; i++){
        int y;
        unordered_map<string, double> prods;
        cin >> y;
        for (int j = 0; j<y; j++){
            string produto;
            double preco;
            cin >> produto;
            cin >> preco;
            prods[produto] = preco;
        }
        int z;
        double val = 0.0;
        cin >> z;
        for (int k = 0; k < z; k++){
            string prodc;
            double quant;
            cin >> prodc;
            cin >> quant;
            val += quant*prods[prodc];
        }
        cout << "R$ " << fixed << setprecision(2) << val << endl;
    }
}
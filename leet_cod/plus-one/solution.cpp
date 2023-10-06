#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

vector<int> plusOne(vector<int>& digits) {
    vector<int> lista;
    bool soma_um = true;
    for (int i = digits.size() - 1; i >= 0; i--) {
        if (soma_um) {
            int x = digits[i] + 1;
            if (x == 10) {
                lista.push_back(0);
            }
            else {
                lista.push_back(x);
                soma_um = false;
            }
        }
        else {
            lista.push_back(digits[i]);
        }
    }
    if (soma_um) {
        lista.push_back(1);
    }
    reverse(lista.begin(), lista.end());
    return lista;
}

int main() {
    vector<int> digits = { 1, 2, 3 };
    vector<int> result = plusOne(digits);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
}
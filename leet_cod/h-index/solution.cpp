#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int tam = citations.size();
        for (int i = 0; i<tam; i++){
            if (citations[i] >= tam-1){
                return tam - 1;
            }
        }
    };
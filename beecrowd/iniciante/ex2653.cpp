#include <bits/stdc++.h>

using namespace std;

int main(){
    set<string> conjunto;
    string joia;
    while(getline(cin,joia))
    {
        conjunto.insert(joia);
    }
    cout << conjunto.size() << endl;
    return 0;
}
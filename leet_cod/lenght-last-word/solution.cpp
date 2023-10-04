#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

int lengthOfLastWord(string s) {
        int i = s.size()-1;
        int tam = 0;
        if (i == -1)
            return tam;
        while (s[i] == ' ')
        {
            i--;
            if (s[i] == 0)
                return tam;
        }
        
        while (s[i] != ' ')
        {
            tam +=1;
            if (i==0){
                return tam;
            }
            i--;
        }
        return tam;
    }

int main(){
    string a = "teste";
    cout << lengthOfLastWord("teste") << endl;
}
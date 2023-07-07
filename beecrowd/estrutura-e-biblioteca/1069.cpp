#include <bits/stdc++.h>

using namespace std;
 
int main(){
    int x;
    cin >> x;
    stack<string> dimas;
    for (int i = 0; i < x; i++){
            stack<char> dimas;
            string coareia;
            int j=0, tot = 0;
            cin >> coareia;
            while (true)
            {
                if (coareia[j]=='.'){
                    j++;
                    continue;
                }
                else if (coareia[j] == '<'){
                    dimas.push(coareia[j]);
                    j++;
                    continue;
                }
                else if(coareia[j] == '>'){
                    if (!dimas.empty()){
                        tot++;
                        j++;
                        dimas.pop();
                    }
                    else{
                        j++;
                    }
                    continue;;
                }
                else
                    break;
            }
            cout << tot << endl;
    }
    return 0;
}
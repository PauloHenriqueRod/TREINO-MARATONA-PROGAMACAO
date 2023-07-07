#include <bits/stdc++.h>

using namespace std;

int main(){
    int x;
    std::cin>>x;
    if (x%2==0){
        x+=1;
    }

    for (int i = 0; i<6; i+=1){
        std::cout << x << "\n";
        x+=2;
    }
    return 0;
    }

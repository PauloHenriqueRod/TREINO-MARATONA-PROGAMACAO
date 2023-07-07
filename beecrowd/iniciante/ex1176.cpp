#include <bits/stdc++.h>

using namespace std;



long long int dp[101010];


long long fib(int N){
    if (N==0){
        return 0;
    }

    if (N==1){
        return 1;
    }

    if (dp[N] != 0)
        return dp[N];
 
    return dp[N] = fib(N - 1) + fib(N - 2);
}   

int main(){
    int NUM;
    int X;
    cin >> NUM;
    for (int i=0; i<NUM; i++){
        cin >> X;
        long long FIBORESP = fib(X);
        cout << "Fib(" << X << ") = " << FIBORESP << endl;
    }
    return 0;
}
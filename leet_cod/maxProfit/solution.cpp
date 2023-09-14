#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <string>
#define optimize ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)

using namespace std;

int maxProfit(vector<int>& prices) {
    int min_price = prices[0];
    int profit = 0;
    for(auto price: prices){
        min_price = min(min_price, price);
        profit = max(profit, price-min_price);
    }
    return profit;
    }

int main()
{
    optimize;
    std:: vector<int> lista = {7,6,4,3,1};
    int b = maxProfit(lista);
    cout << b << endl;
    return 0;
}
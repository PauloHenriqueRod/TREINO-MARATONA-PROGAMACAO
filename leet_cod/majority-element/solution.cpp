#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

int majorityElement(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int a = nums.size();
    int m = a/2;
    return nums[m];
    }


int main(){
    std:: vector<int> lista = {0,0,1,1,1,2,2,3,3,4};
    int b = majorityElement(lista);
    cout << b << endl;
}

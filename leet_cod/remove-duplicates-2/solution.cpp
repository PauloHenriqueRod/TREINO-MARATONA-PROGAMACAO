#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <string>
#define endl '\n'


using namespace std;
using namespace __gnu_pbds;

int removeDuplicates(vector<int>& nums) {
    int tam = nums.size();
    if(tam == 1)
        return 1;
    int count = 0;
    vector<int> numsaux;
    numsaux.emplace_back(nums[0]);
    numsaux.emplace_back(nums[1]);
    for(int i = 2; i<tam; i++){
        if(nums[i]!=nums[i-2]){
            numsaux.emplace_back(nums[i]);
            count++;
        }
    }
    for(int i = 0; i<count+2; i++){
        nums[i] = numsaux[i];
    }

    nums.resize(count+2);
    return count+2;
}

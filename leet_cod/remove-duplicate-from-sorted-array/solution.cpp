#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <string>
#define endl '\n'


using namespace std;
using namespace __gnu_pbds;
int removeDuplicates(vector<int>& nums) {
    int tam = nums.size();
    int count = 0;
    vector<int> numsaux;
    numsaux.emplace_back(nums[0]);
    for(int i = 1; i<tam; i++){
        if(nums[i]!=nums[i-1]){
            numsaux.emplace_back(nums[i]);
            count++;
        }
    }
    for(int i = 0; i<count+1; i++){
        nums[i] = numsaux[i];
    }

    nums.resize(count+1);
    return count+1;
}

int main(){
    std:: vector<int> lista = {0,0,1,1,1,2,2,3,3,4};
    int b = removeDuplicates(lista);
    for(auto a: lista){
        cout << a << endl;
    }
    cout << b << endl;
}
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

vector<int> productExceptSelf(vector<int>& nums) {
    int quant_zeros = 0;
    int produto = 1;
    vector<int> nums_final = {};
    for (int i=0; i<nums.size(); i++ ){
        if(nums[i] == 0){
            quant_zeros += 1;
            continue;
        }
        produto = produto*nums[i];
    }
    if (quant_zeros>1){
        for (int i = 0; i<nums.size(); i++){
            nums_final.emplace_back(0);
        }
        return nums_final;
    }
    if (quant_zeros==1){
        for (int i = 0; i<nums.size(); i++){
            if (nums[i] == 0){
                nums_final.emplace_back(produto);
                continue;
            }
            nums_final.emplace_back(0);
        }
        return nums_final;
    }
    for (int i = 0; i<nums.size(); i++){
        int x = produto/nums[i];
        nums_final.emplace_back(x);
        }
        return nums_final;
    return nums_final;
    }


int main(){
    vector<int> lista = {-1, 0, 1,-3,3};
    vector<int> lista_2 = productExceptSelf(lista);
    for (int i = 0; i<lista.size(); i++){
        cout << lista_2[i] << endl;
    }
}
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <string>
#define endl '\n'


using namespace std;
using namespace __gnu_pbds;

int removeElement(vector<int>& nums, int val) {
    int index = 0;
    for(int i = 0; i<nums.size(); i++){
        if (nums[i] != val){
            nums[index] = nums[i];
            index++;
        }
    }
        nums.resize(index);
        return index;
    }


int main(){
    std:: vector<int> lista = {0,1,2,2,3,0,4,2};
    int b = removeElement(lista, 2);
    for (auto a: lista){
        cout << a << endl;
    }
    cout << b << endl;
}
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

bool canJump(std::vector<int>& nums) {
    if (nums.empty() || nums.size() == 1) {
        return true;
    }

    int maximo = 0;
    int tot = nums.size();

    for (int j = 0; j < tot; ++j) {
        maximo = std::max(maximo, nums[j]);

        if (nums[j] == 0) {
            if (maximo == 0) {
                return false;
            }
        }

        if (maximo >= tot - j - 1) {
            return true;
        }

        maximo -= 1;
    }

    return true;
}
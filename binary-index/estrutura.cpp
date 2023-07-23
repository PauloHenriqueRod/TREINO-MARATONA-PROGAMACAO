#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int MAXN = 2e5 + 5;
 
ll bit[MAXN];
ll arr[MAXN];
 
void upd(int x, ll v){
	while(x < MAXN){
		bit[x] += v;
		x += (x & -x);
	}
}
 
ll qry(int x){
	ll ret = 0;
 
	while(x > 0){
		ret += bit[x];
		x -= (x & -x);
	}
	return ret;
}
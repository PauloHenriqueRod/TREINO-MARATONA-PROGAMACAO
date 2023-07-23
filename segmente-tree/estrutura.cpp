#include <bits/stdc++.h>
using namespace std;
 
const int MAXN = 2e5 + 100;
typedef long long ll;
 
ll tree[4 * MAXN];
int arr[MAXN];
 
void update(int pos, int i, int j, int x, ll val){
	int esq = 2*pos;
	int dir = 2*pos + 1;
	int mid = (i+j)/2;
 
	tree[pos] += val;
 
	if(i == j) return;
	if(x <= mid) update(esq, i, mid, x, val);
	else update(dir, mid+1, j, x, val);
}
 
ll query(int pos, int i, int j, int l, int r){
	int esq = 2*pos;
	int dir = 2*pos + 1;
	int mid = (i+j)/2;
 
	if(i > r || j < l) return 0;
	if(i >= l && j <= r) return tree[pos];
	else return query(esq, i, mid, l, r) + query(dir, mid+1, j, l, r);
}
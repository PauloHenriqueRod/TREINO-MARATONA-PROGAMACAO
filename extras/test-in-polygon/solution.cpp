#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define ll long long

struct pt { // ponto
	int x, y;
	pt(int x_ = 0, int y_ = 0) : x(x_), y(y_) {}
	bool operator < (const pt p) const {
		if (x != p.x) return x < p.x;
		return y < p.y;
	}
	bool operator == (const pt p) const {
		return x == p.x and y == p.y;
	}
	pt operator + (const pt p) const { return pt(x+p.x, y+p.y); }
	pt operator - (const pt p) const { return pt(x-p.x, y-p.y); }
	pt operator * (const int c) const { return pt(x*c, y*c); }
	ll operator * (const pt p) const { return x*(ll)p.x + y*(ll)p.y; }
	ll operator ^ (const pt p) const { return x*(ll)p.y - y*(ll)p.x; }
	friend istream& operator >> (istream& in, pt& p) {
		return in >> p.x >> p.y;
	}
};


typedef pair<long long,long long int> ponto;
typedef vector<ponto> poligono;


long long int e_esquerda(ponto a, ponto b, ponto c){
    long long int det = (b.x-a.x)*(c.y-a.y) - (c.x-a.x)*(b.y-a.y);
    if (det>0) return 1; // c esta a esquerda
    if (det<0) return -1; // c esta a direita
    return 0; // pontos colineares
}

int inpol(vector<pt>& v, pt p) { // O(n)
    int qt = 0;
    for (int i = 0; i < v.size(); i++) {
        if (p == v[i]) return 2;
        int j = (i+1)%v.size();
        if (p.y == v[i].y and p.y == v[j].y) {
            if ((v[i]-p)*(v[j]-p) <= 0) return 2;
            continue;
        }
        bool baixo = v[i].y < p.y;
        if (baixo == (v[j].y < p.y)) continue;
        auto t = (p-v[i])^(v[j]-v[i]);
        if (!t) return 2;
        if (baixo == (t > 0)) qt += baixo ? 1 : -1;
    }
    return qt != 0;
}


int main(){
    int n, m;
    int x, y;
    cin >> n >> m;
    vector<pt> pol;
    for(int i = 0; i< n; i++){
        cin >> x >> y;
        pt p(x, y);
        pol.push_back(p);
    }
    for(int i = 0; i<m; i++){
        cin >> x >> y;
        pt p(x, y);
        if(inpol(pol, p) == 0)
            cout << "OUTSIDE" << endl;
        if(inpol(pol, p) == 2)
            cout << "BOUNDARY" << endl;
        if(inpol(pol, p) == 1)
            cout << "INSIDE" << endl;
    }
}
;
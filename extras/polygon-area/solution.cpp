#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second

typedef pair<long long,long long int> ponto;
typedef vector<ponto> poligono;

long long int area_polygon(poligono p){
    int n = p.size();
    long long int area = 0.0;
    for (int i = 0; i<n ; i++){
        ponto p1 = p[i], p2 = p[(i+1)%n];
        area += (p2.x+p1.x)*(p2.y-p1.y);
    }
    return abs(area);
}

int main(){
    int n;
    cin >> n;
    poligono pol;
    for(int i = 0; i<n; i++){
        ponto p;
        cin >> p.x >> p.y;
        pol.push_back(p);
    }
    cout << area_polygon(pol) << endl;
}
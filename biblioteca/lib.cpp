#include <bits/stdc++.h>
using namespace std;
// para definir pontos
#define x first
#define y second
// para definir linhas
#define a_num first.first
#define a_denm first.second
#define b second

/*
setprecision = numero de casas flutuantes
fixed = fixa a notação que vai ser impressa
Para fazer comparações de números double utilizar o EPS(número bem pequeno)
abs(x) < EPS
abs(x-y) < EPS
const double pi = acos(-1) 
*/

typedef pair<int,int> ponto;
typedef pair<pair<int, int>, int> linha;
typedef vector<ponto> poligono;


int calculo_mmc(int a, int b){ /* Algoritmo de Euclides para cálculo de mmc O(log(n))*/
    while (b) {
        int temp = a;
        a = b;
        b = temp % b;
    }
    return a;
}

bool eh_primo(int n){
    if (n<=1)
        return false;
    if (n<=3)
        return true;
    if (n%2 == 0 || n%3 == 0)
        return false;
    int i = 5;
    while (i*i<=n)
    {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
        i = i+6;
    }
    return true;
}

int contarDigitos(int numero) {
    /*Função que conta o número de digitos de uma função*/
    if (numero == 0) {
        return 1;
    }

    int quantidade_de_digitos = static_cast<int>(log10(std::abs(numero))) + 1; /*Precisa da biblioteca cmath*/
    return quantidade_de_digitos;
}

int qtdDiv(long long n){
    int res = 0;
    for(int i=1; i<=n/i; i++){
        if(n%i == 0){
            if(i*1LL*i == n)
                res = res + 1;
            else
                res = res + 2;
        }
    }
    return res;
}

vector<long long> fatores(long long n){
    vector<long long> res;
    for(int i=2; i<=n/i; i++){
        while(n%i == 0){
            res.push_back(i);
            n = n/i;
        }
    }
    if(n > 1)
        res.push_back(n);
    return res;
}

double modulo(ponto p){
    return sqrt(p.x*p.x + p.y*p.y);
}

ponto vetor_ligante(ponto p, ponto q){
    // Função para encontrar o vetor que vai de "1" para "2"
    ponto vetor;
    vetor.x = p.x-q.x;
    vetor.y = p.y-q.y;
    return vetor;
}

double angulo_vetor(ponto p){
    return (double) p.y/ (double) p.x;
}

int prodEscalar(ponto p, ponto q){
    // Prod interno
    return p.x*q.x + p.y*q.y;
}

int prodVetorial(ponto p, ponto q){
    return p.x*q.y - q.x*p.y;
}

double tamProjecao(ponto p, ponto q){
    // Calcula o tamanho da projeção de a em b
    return prodEscalar(p, q)/modulo(q);
}


// Vetor de projeção de A em B
// Pra usar isso os pontos devem ser em double
/*
pair<double, double> vetProjecao(double x1, double x2, double y1, double y2){
    pair<double, double> novoVetor;
    novoVetor.first = (x2/modulo(x2, y2))*tamProjecao(x1,x2,y1,x2);
    novoVetor.second = (y2/modulo(x2, y2))*tamProjecao(x1,x2,y1,x2);
    return novoVetor;
}
*/
const int AGUDO = 1, RETO = 0, OBTUSO = -1; //<90, =90, >90

int tipoAngulo(ponto p, ponto q){
    int res = prodEscalar(p, q);
    if(res>0)
        return AGUDO;
    if(res == 0)
        return RETO;
    return OBTUSO;
}

int areaPalalelogramo(ponto p, ponto q){
    // Função que encontra a área formada pela projeção dos 2 vetores
    return abs(prodVetorial(p, q));
}

double areaTriangulo(ponto p, ponto q){
    return (double) areaPalalelogramo(p, q)/2.0;
}

bool perpedicular(ponto p, ponto q){
    return prodEscalar(p, q) == 0;
}

bool paralelo(ponto p, ponto q){
    return prodVetorial(p, q) == 0;
}

// Encontra a equação da reta que passa pelos pontos p e q
pair<double, double> equacao_reta(ponto p, ponto q){
    double a = (p.y-q.y) / (p.x-q.x);
    double b = p.y - (a*p.x);
    return {a, b};
}

// Lei dos cossenos para encontrar o angulo que forma duas retas
double angle_a(int a, int b, int c){
    return acos(double(a*a - b*b - c*c)/double(-2*b*c));
}

// Distancia ponto e reta(que passa pelos pontos p1 e p2)
double dist_p1(ponto p1, ponto p2, ponto q){
    double num = abs((p2.y-p1.y)*q.x - (p2.x-p1.x)*q.y + p2.x*p1.y - p2.y*p1.x);
    double den = sqrt((p2.y-p1.y)*(p2.y-p1.y) + (p2.x-p1.x)*(p2.x-p1.x));
    return num/den;
}

// Calcula a area de um poligono p, com a formula de gauss
double area_polygon(poligono p){
    int n = p.size();
    double area = 0.0;
    for (int i = 0; i<n ; i++){
        ponto p1 = p[i], p2 = p[(i+1)%n];
        area += (p2.x+p1.x)*(p2.y-p1.y);
    }
    area /= 2.0;
    return abs(area);
}
//produto vetorial entre 3 vetores



// Teste esquerda
int e_esquerda(ponto a, ponto b, ponto c){
    int det = (b.x-a.x)*(c.y-a.y) - (c.x-a.x)*(b.y-a.y);
    if (det>0) return 1; // c esta a esquerda
    if (det<0) return -1; // c esta a direita
    return 0; // pontos colineares
}

// checa se o ponto q está dentro do polígomo
int ta_dentro(ponto p, poligono pol){
    int n = pol.size();
    for (int i = 0; i<n ; i++){
        if(e_esquerda(pol[i], pol[(i+1)%n], p) == -1)
            return false;
    }
    return true;
}





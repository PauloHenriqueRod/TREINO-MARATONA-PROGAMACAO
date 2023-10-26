#include <bits/stdc++.h>
using namespace std;


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

double modulo(int x, int y){
    return sqrt(x*x + y*y);
}


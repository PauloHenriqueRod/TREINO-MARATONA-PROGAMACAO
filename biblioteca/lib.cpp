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

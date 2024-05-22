#include <iostream>
#include <vector>
#include <cmath>

int paridade(int x) {
    int n = 2;
    int par = 0;
    while (n <= x) {
        par += x / n;
        n *= 2;
    }
    return par;
}

int count_primos(int n, int m) {
    if (!(n > m)) {
        int aux = n;
        n = m;
        m = aux;
    }
    if (n <= 1) {
        return 0;
    }

    std::vector<int> prime(n + 1, 1);
    prime[0] = prime[1] = 0;

    for (int i = 2; i <= sqrt(n); ++i) {
        if (prime[i] == 1) {
            for (int j = i * i; j <= n; j += i) {
                prime[j] = 0;
            }
        }
    }

    int sum_primes = 0;
    for (int i = m; i <= n; ++i) {
        sum_primes += prime[i];
    }

    return sum_primes;
}

int main() {
    int n, m;
    std::cin >> n >> m;
    int x = abs(n - m);
    if (x == 0) {
        std::cout << '?' << std::endl;
    } else {
        int quant_primos = count_primos(n, m);
        if (quant_primos == 0) {
            std::cout << "Bob" << std::endl;
        } else {
            int resposta = paridade(quant_primos + x - 1) - (paridade(x) + paridade(quant_primos - 1));
            if (resposta > 0) {
                std::cout << "Bob" << std::endl;
            } else {
                std::cout << "Alice" << std::endl;
            }
        }
    }
    return 0;
}
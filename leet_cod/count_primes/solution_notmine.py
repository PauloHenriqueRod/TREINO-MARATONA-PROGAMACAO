'''
credits: https://leetcode.com/problems/count-primes/solutions/5047315/what-is-sieve-of-eratosthenes-explanation-theory-and-steps
'''

def countPrimes(n):
    if n <= 1:
        return 0

    prime = [1]*n
    prime[0] = prime[1] = 0 # prime[0] = 0 and prime[1] = 1

    for i in range(2,int(n**0.5) + 1):
        if prime[i] == 1:
            for j in range(i**2, n, i):
                prime[j] = 0
    return sum(prime)

print(countPrimes(5000000))
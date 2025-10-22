def PrimeList(N):
    primes = []
    for num in range(2, N):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)
n = int(input("请输入正整数 N: "))
result = PrimeList(n)
print(result)

    

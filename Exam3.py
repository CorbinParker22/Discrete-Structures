def prime_numbers(n):
    ctr = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

n = 10
print('Number of primes under 10 are:', (prime_numbers(n)))
n = 100
print('Number of primes under 100 are:', (prime_numbers(n)))
n = 1000
print('Number of primes under 1,000 are:', (prime_numbers(n)))
print('calculating...')
n = 100000
print('Number of primes under 100,000 are:', (prime_numbers(n)))
print('(couldnt do 100,000,000 because it took too long for my computer to calculate)')

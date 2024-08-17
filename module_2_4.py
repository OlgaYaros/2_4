numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 1
for i in range(1, len(numbers)):  # число
    if (numbers[i] >= 2):
        for j in range(2, ((int(i) ** 2) + 1)):  # делители
            if (numbers[i] % j == 0):
                    is_prime += 1
        if is_prime == 1:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
    is_prime = 0
print(primes)
print(not_primes)
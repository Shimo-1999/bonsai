is_prime = [True for _ in range(10**4 + 1)]
is_prime[0] = False
is_prime[1] = False
prime_numbers = []
for i in range(10**4 + 1):
    if is_prime[i]:
        prime_numbers.append(i)
        for j in range(2 * i, 10**4 + 1, i):
            is_prime[j] = False

n = int(input())
count = 0
for _ in range(n):
    m = int(input())
    for prime_number in prime_numbers:
        if m % prime_number == 0 and m != prime_number:
            break
    else:
        count += 1
print(count)

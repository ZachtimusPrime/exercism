
def sieve(limit: int) -> list:
    if limit < 2:
        return []

    primes = []
    nums = list(range(2, limit+1))
    for index in range(2, limit+1):
        if index in nums:
            primes.append(index)
            for num in nums:
                if num % index == 0:
                    nums.remove(num)

    return primes

print(sieve(99999))
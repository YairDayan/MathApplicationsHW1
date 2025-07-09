##### 1 #####

def is_prime(num):
    # Check if a number is prime
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_factors(n):
    # Find the prime factors of a number and return them as a formatted string
    n = int(n)
    if n == 1: return "1 has no prime multipliers"
    i = 2
    result = ""
    while n > 1:
        count = 0
        # Count the number of times num is divisible by i
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            # Append the prime factor and its count to the result string
            if count == 1:
                result += str(i)
            else:
                result += str(i) + "^" + str(count)
            if n > 1:
                result += "*"
        i += 1
        # Find the next prime number
        while not is_prime(i):
            i += 1
    return result

user_num = input("Please enter your number: ")
print(prime_factors(user_num))

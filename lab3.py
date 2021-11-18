# Zad1
# def numbers(n: int):
#     if n < 0:
#         return
#     print(n)
#     numbers(n-1)

# numbers(8)

# Zad2
# def fib(n: int) -> int:
#     if n < 0:
#         return
#     if n == 1 or n == 2:
#         return 1
#     if n > 2:
#         return fib(n - 1) + fib(n - 2)

# print(fib(5))

# Zad3
# def power(number: int, n: int) -> int:
#     if n == 0:
#         return 1
#     return power(number, n - 1) * number

# print(power(2, 3))

# Zad4
# def reverse(txt: str) -> str:
#     if txt == "":
#         return txt
#     return txt[-1] + reverse(txt[:-1])

# print(reverse("bagno"))

# Zad5
# def factorial(n: int) -> int:
#     if n == 1:
#         return 1
#     return factorial(n - 1) * n

# print(factorial(4))

# Zad6
def prime(n: int) -> bool:
    def pom(n: int, i: int) -> bool:
        if i < 2:
            return True
        if n % i == 0:
            return False
        return pom(n, i - 1)

    if n == 1:
        return False
    if n > 1:
        return pom(n, n-1)

print(prime(6))

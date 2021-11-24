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

# def prime(n: int) -> bool:
#     def pom(n: int, i: int) -> bool:
#         if i < 2:
#             return True
#         if n % i == 0:
#             return False
#         return pom(n, i - 1)

#     if n == 1:
#         return False
#     if n > 1:
#         return pom(n, n-1)

# print(prime(7))

# Zad7

# def n_sums(n: int) -> "list[int]":
#     def check(liczba: int) -> bool:
#         suma1 = 0
#         suma2 = 0
#         counter = 0
#         for j in str(liczba):
#             if counter % 2 == 0:
#                 suma1 += int(j)
#                 counter += 1
#                 continue
#             if counter % 2 == 1:
#                 suma2 += int(j)
#                 counter += 1
#                 continue
#         if suma1 == suma2:
#             return True
#         return False
#     def create(n: int) -> list:
#         return list(range(10**(n-1), 10**n))
#     def div(lista: list) -> list:
#         return lista[1:]
#     def logic(list1: list, lista1: list):
#         liczba = lista1[0]
#         lista1 = div(lista1)
#         if check(liczba) is True:
#             list1.append(liczba)
#         if lista1 == []:
#             return list1
#         return logic(list1, lista1)
#     list1 = []
#     lista1 = create(n)
#     return logic(list1, lista1)
# 
# print(n_sums(3))

# lista = list(range(10**4, 10**5))
# for i in lista:
#     suma1 = 0
#     suma2 = 0
#     counter = 0
#     for j in str(i):
#         if counter % 2 == 0:
#             suma1 += int(j)
#             counter += 1
#             continue
#         if counter % 2 == 1:
#             suma2 += int(j)
#             counter += 1
#             continue
#     if suma1 == suma2:
#         print(i)

# Zad8

# Zad9

# def remove_duplicates(txt: str) -> str:
#     if len(txt) < 2:
#         return txt
#     if txt[0] != txt[1]:
#         return txt[0] + remove_duplicates(txt[1:])
#     return remove_duplicates(txt[1:])
    
# print(remove_duplicates("XXXTTYXY"))

# Zad10

# def balanced_parantheses(n: int) -> str:
#     def logic(n: int, txt: str, curr: int) -> str:
#         if n == 0:
#             if curr == 0:
#                 return txt
#             return logic(n, txt + ")", curr - 1)
#         if curr == 0:
#             return logic(n - 1, txt + "(", curr + 1)
#         return logic(n - 1, txt + "(", curr + 1) + logic(n, txt + ")", curr - 1)
#     def tostr(n: int, txt: str) -> str:
#         return "\n".join(txt[i:i+n] for i in range(0, len(txt), n))
#     if n % 2 == 1:
#         return "No possible combinations"
#     return tostr(n, logic(n/2, "", 0))


# print(balanced_parantheses(6))

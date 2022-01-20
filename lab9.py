from typing import List

"""
Sortowanie bombelkowe

Wejscie: [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]

Krok1:
()
"""

def bubble_sort(l: List):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] < l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp

def bubble_sort_reverse(l: List):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp

def selection_sort(l: List):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        tmp = l[i]
        l[i] = l[min_index]
        l[min_index] = tmp

def selection_sort_reverse(l: List):
    for i in range(len(l)):
        max_index = i
        for j in range(i + 1, len(l)):
            if l[j] > l[max_index]:
                max_index = j
        tmp = l[i]
        l[i] = l[max_index]
        l[max_index] = tmp

def insertion_sort(l: List):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j = j - 1
            l[j + 1] = key

def insertion_sort_reverse(l: List):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] < key:
            l[j + 1] = l[j]
            j = j - 1
            l[j + 1] = key

lista = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]

insertion_sort_reverse(lista)
print(lista)

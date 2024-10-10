import random


class Tablica:
    def __init__(self, n):
        self.n = n
        self.tablica = [0] * n

    def wypelnij(self,a,b):
        self.tablica = [random.randint(a,b) for _ in range(self.n)]

    def maksimum(self):
        return max(self.tablica)

    def minimalna(self):
        return min(self.tablica)

    def maksimum2(self):
        unikalne = list(set(self.tablica))
        unikalne.sort(reverse=True)
        return unikalne[0], unikalne[1]

    def znajdowanie_liczby(self,a):
        try:
            return  self.tablica.index(a)
        except ValueError:
            return -1

tab = Tablica(10)
tab.wypelnij(1,100)
print(tab.tablica)
print(tab.maksimum())
print(tab.minimalna())
print(tab.maksimum2())
print(tab.znajdowanie_liczby(50))
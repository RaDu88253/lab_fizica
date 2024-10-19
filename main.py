import matplotlib.pyplot as plt
from util import *

marime_fizica_ox = input("Introduceti o marime fizica pentru Ox: ")
unitate_ox = input("\nIntroduceti o unitate de masura pentru Ox: ")

marime_fizica_oy = input("\nIntroduceti o marime fizica pentru Oy: ")
unitate_oy = input("\nIntroduceti o unitate de masura pentru Oy: ")

n = int(input("\nCate masuratori vrei sa introduci? "))
x = []
y = []
print(f"\nIntrodu {n} valori pentru axa Ox (separate prin Enter): ")
for i in range(n):
	x.append(float(input()))
print(f"\nIntrodu {n} valori pentru axa Oy (separate prin Enter):")
for i in range(n):
	y.append(float(input()))

plt.xlabel(marime_fizica_ox + ' (' + unitate_ox + ')')
plt.ylabel(marime_fizica_oy + ' (' + unitate_oy + ')')

plt.scatter(x, y, marker='x', color='red')
plt.title(marime_fizica_oy + " in functie de " + marime_fizica_ox)

m, n = linear_regression(n, x, y)

x_f = [min(x), max(x)]
y_f = [m * x_f[0] + n, m * x_f[1] + n]

plt.plot(x_f, y_f)

print(f"Panta este {m} {unitate_oy}/{unitate_ox}")
print(f"Ordonata la origine este {n} {unitate_oy}")

plt.show()

import matplotlib.pyplot as plt


marime_fizica_ox = input("Introduceti o marime fizica pentru Ox: ")
unitate_ox = input("Introduceti o unitate de masura pentru Ox: ")

marime_fizica_oy = input("Introduceti o marime fizica pentru Oy: ")
unitate_oy = input("Introduceti o unitate de masura pentru Oy: ")

x = [1, 2, 5]
y = [10, 20, 30]

plt.xlabel(marime_fizica_ox + ' (' + unitate_ox + ')')
plt.ylabel(marime_fizica_oy + ' (' + unitate_oy + ')')

plt.scatter(x, y, marker='x', color='red')

plt.title(marime_fizica_oy + " in functie de " + marime_fizica_ox)

plt.show()
